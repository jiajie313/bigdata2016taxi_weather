# Educational Purposes

Demonstrate the fundamental usage of Hadoop/Spark and data visualization techniques.

# Part-I Taxi Facts

**Generally speaking, where are the highly served regions?**

Two heatmap plots: one is for pick-up positions, the other is for drop positions. From visualization, we could further ask:

- is there any "danger" places where no taxis enter/exit?
- is the pattern changed along time (in years/months)?

**Individually speaking, is there any serving preference given certain driver?**

Heatmap: territories of certain driver v.s. average drivers.

If exists, we could design a service for these drivers which could guide them to locations with potential service needs. In other words, could we design a smart "customer-radar" for drivers? See following.

# Part-II Heart-beating of New York City

**Within a day, is there any changes of service pattern?**

- Trend plot. x axis is time(hour), y axis could be the total number of trips.
- Dynamic heatmap. Given time period, generating the heatmap is same as Part-I. But using D3.js or other visualization platforms to demonstrate the heart-beat of NYC.
    + Taxi data
    + CityBike data

If pattern changes along time, we could offer these information to drivers so that they could go to locations where highly in needs during given period of time.

# Part-III Taxi usage and climate

Correlation of taxi usage and climate probably exists (based on the literature shown in class), therefore **could we use the taxi usage to predict the time temperature?**

Time-series data:

- Taxi/CityBike usage along the hour
- Temperature/raining status along the hour

Apply neural networks (e.g. RNN).

# Summary

| Part  | Time is __    | Location is __| Focus     |
|------ |------------   |------------   |--------   |
| I     | Aggregated    | Aggregated    | Past      |
| II    | Dynamic       | Dynamic       | Now       |
| III   | Dynamic       | Aggregated    | Future    |







