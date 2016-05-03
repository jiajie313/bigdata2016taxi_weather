library(ggmap)
infile <- file.path(getwd(), 'data/201501-citibike-tripdata.csv')
citibike201501 <- read.csv(infile, stringsAsFactors=FALSE)

start_lat_min <- min(citibike201501$start.station.latitude)
start_lat_max <- max(citibike201501$start.station.latitude)
start_lon_min <- min(citibike201501$start.station.longitude)
start_lon_max <- max(citibike201501$start.station.longitude)

plot_lat_bt  <- start_lat_min - 2
plot_lat_up  <- start_lat_max + 2
plot_lon_lft <- start_lon_min - 2
plot_lon_rit <- start_lat_max + 2

## Static Scatter Plot
png(filename = file.path(getwd(), 'fig/scatter_plot.png'),
    width = 850, height = 1100)
q <- qmplot(start.station.longitude, start.station.latitude,
       data = citibike201501, maptype = "toner-lite", color = I("red"))
print(q)
dev.off()

## Thematic Plot
png(filename = file.path(getwd(), 'fig/thematic_plot.png'),
    width = 850, height = 1100)
q <-
qmplot(start.station.longitude, start.station.latitude,
       data = citibike201501, maptype = "toner-lite",
       geom = "blank", zoom = 14,
       legend = "bottom") +
  stat_density_2d(aes(fill = ..level..),
                  geom = "polygon", alpha = .3, color = NA) +
  scale_fill_gradient2("Pick-Up Activities",
                       low = "ghostwhite", mid = "yellow", high = "red")
print(q)
dev.off()
