import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from sklearn.preprocessing import StandardScaler
from causallearn.search.ScoreBased.GES import ges
from causallearn.utils.GraphUtils import GraphUtils
from econml.iv.nnet import DeepIV
from scipy.stats import pearsonr

#data preprocessing
df = pd.read_csv("bird_climate_data.csv")
for lag in [1, 3, 6, 12]:
    df[f"fish_lag_{lag}"] = df["fish_population"].shift(lag)
    df[f"temp_lag_{lag}"] = df["temperature"].shift(lag)

#standardize data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df.dropna())
df = pd.DataFrame(df_scaled, columns = df.columns)
df.dropna(inplace = True)

#learn dag structure
data_matrix = df.values
cg = ges(data_matrix)
GraphUtils.draw_graph(cg)

def extract_val_from_dag(graph, target_var):
    val = []
    for edge in graph.G.edges:
        if edge[1] == target_var:
            val.append(edge[0])
    return val

val_ = extract_val_from_dag(cg, "osprey_population")
print(f"Osprey Population: {val_}")

#learn structural casual equations
class CausalSEM(nn.Module):
    def __init__(self, input_dim):
        super(CausalSEM, self).__init__()
        self.layer1 = nn.Linear(input_dim, 64)
        self.layer2 = nn.Linear(64, 64)
        self.layer3 = nn.Linear(64, 1)  #output: opulation prediction

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        return self.layer3(x)

#training
X_train_causal = df[val_].values
y_train = df["osprey_population"].values

X_train_causal = torch.tensor(X_train_causal, dtype = torch.float32)
y_train = torch.tensor(y_train, dtype = torch.float32).view(-1, 1)

model = CausalSEM(input_dim = X_train_causal.shape[1])
optimizer = optim.Adam(model.parameters(), lr = 0.001)
loss_fn = nn.MSELoss()

for epoch in range(500):
    optimizer.zero_grad()
    predictions = model(X_train_causal)
    loss = loss_fn(predictions, y_train)
    loss.backward()
    optimizer.step()

#causal effect estimation
corr, p_val = pearsonr(df["fish_population"], df["osprey_population"])
print(f"Strength (Fish Population vs Osprey Population): r={corr}, p={p_val}")

if p_val > 0.05:
    raise ValueError("Fish population is not a strong IV.")

#training
deep_iv = DeepIV(n_hidden = 128, n_layers = 3, optimizer = "adam")
deep_iv.fit(X_train_causal, df["fish_population"].values, df["osprey_population"].values)

#counterfactual. ex: what if fish availability drops 20%?
X_test_counterfactual = X_train_causal.clone()
X_test_counterfactual[:, df.columns.get_loc("fish_population")] *= 0.8  #reduce fish by 20%

y_counterfactual = deep_iv.predict(X_test_counterfactual)
print(f"Counterfactual Osprey Population: {y_counterfactual.mean()}")

#forcasting
class BirdForecastingModel(nn.Module):
    def __init__(self, input_size, hidden_dim=128, num_layers=3):
        super(BirdForecastingModel, self).__init__()
        self.transformer = nn.Transformer(d_model = hidden_dim, nhead = 8, num_encoder_layers = num_layers)
        self.fc_out = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        x = self.transformer(x, x)
        return self.fc_out(x)

forecast_model = BirdForecastingModel(input_size = len(val_))

#forecasting 50 years ahead under climate change
X_forecast = df[val_].values.copy()
X_forecast[:, df.columns.get_loc("temperature")] += 3  #simulate +3°C warming

X_forecast_tensor = torch.tensor(X_forecast, dtype = torch.float32)
future_osprey = forecast_model(X_forecast_tensor).detach().numpy()
print(f"Projected Osprey Population Under +3°C Warming: {future_osprey.mean()}")