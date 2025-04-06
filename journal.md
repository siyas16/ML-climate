**February 23, 2025 - Siya**

We spent the week looking around for data sources we could use for our project. Right now, we're considering using multiple datasets and basically overlaying/combining them for the study we want to do. Since we're trying to study how climate change has affected interactions between different bird species, we want data that captures climate change effects (ex: differences in global temperature or differences in extreme weather events) that we could combine with a dataset we found about bird species. That way, we could do a time analysis of how, for example, has interactions between bird species changed in the past x years as the global temperature has risen. I will add the datasets we've found to a file in the etc directory.

**February 24, 2025 - Malini**

Some of the datasets we are looking at include bird migration data from https://science.ebird.org/en/status-and-trends and https://www.usgs.gov/data/2022-release-north-american-breeding-bird-survey-dataset-1966-2021, information about the impact of climate change on certain bird species from https://www.audubon.org/climate/survivalbydegrees, and weather data from https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview and https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily. Given that our topic "Studying effects of climate change on bird species interactions" is still quite broad, we are trying to narrow down what "interaction" means. For example, we could explore species coexistance (do species that used to live near each other still coexist or has climate changed caused them to live further away), competition (are species that compete for the same food or nesting areas overlapping), predator-prey (have there been noticible climate change related food web changes), or breeding/migration (are different bird species now breeding/migrating at the same time due to climate change). We are hoping to figure out the exact question we are exploring and how to combine the datasets we want to use to explore the question this week. 

**March 9, 2025 - Malini**

Last week, we talked about what questions we wanted to explore and decided on focusing on bird species that compete for the same resources. We looked at ecological models about this topic and came across the Resource Ratio Theory or the R* rule by George David Tilman which can be used to model population dynamics for species that compete for the same resource. We also started putting together the datasets by using the average monthly temperature for the past 30 years from Berkeley Earth and bird species observations for the last 30 years from eBird. Next week, we plan to finish compiling the data and start visualizing it. We will also start working on a causal model based on the research we looked at. 

**March 15, 2025 - Siya**

Fell behind on journaling because of midterms, but we're currently trying to decide which bird species in particular we want to focus on. We might be considering coastal birds. More updates to come throughout the week... 

**March 22, 2025 - Malini**

We finalized the coastal bird species we will be researching for the project (Osprey and Bald Eagle) as well as the ecological model (The Resource Ratio Theory (R Rule)) for the causal relationship. The Resource Ratio Theory (R Rule) states that when species compete for the same resource, the species that can persist at the lowest resource level will outcompete others. Both ospreys an bald eagles rely on fish for their main food source, but they hunt for fish differently (ospreys dive for fish while bald eagles scavenge and steal food from ospreys). So, the R* Rule predicts that as fish availability declines due to climate-driven changes in temperature and precipitation, bald eagles, which can survive at lower fish levels, will increase their dominance, which will increase competition and reduce osprey's success in getting fish. Thus, in our causal model, climate variables like temperature and precipitation affect fish populations, which in turn drive competitive interactions between bald eagles and ospreys. We collected the bird and climate data, and talked about collecting the fish data. We are now working on modeling the causal relationship and dicussing our Machine Learning model (probably will be time series based and predict population levels for ospreys and bald eagles 10, 20, and 50 years in the future under varying climate change scenarios).

**March 24, 2025 - Siya**

Wanted to add that we researched other causal models for ecology before we finalized using the R* rule. One such theory was the universal adaptive strategy theory, which states that a 3-way tradeoff that produces adaptive strategies exists between Competitors, Stress tolerators and Ruderals. We felt that our data limited our abilites to use this theory because it was difficult to put the species we're studying into these 3 groups. 

**March 31, 2025 - Siya**

So I spent the week researching different fish species that Osprey and Bald Eagles compete for and how those fish species are being impacted by climate change. I found this report: https://psf.ca/salmon/ that details effects of climate change on pacific salmon specifically. We've decided to focus our research on the Pacific Coast so that we can use the fish data used in this report and because Osprey and Bald Eagles are commonly found on the pacific coast. I've uploaded the fish data we'll be using into the src folder. 

**April 1, 2025 - Malini**

I was sick this weekend, so I didn't have much time to upload what I have been working on. I just uploaded the code for the model I was working on and plan to add information to the document folder. 

**April 6, 2025 - Malini**
We are working on the introduction, hypothesis, and method section of the paper while improving the code to generate the tables/graphs for our paper. 
