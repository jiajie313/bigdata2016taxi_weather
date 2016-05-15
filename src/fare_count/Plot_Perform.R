#
# See the performance of In-Mapper Combiner v.s. Classic
#

library(ggplot2)
theme_set(theme_bw(base_size = 22))
myGthm <- theme(text = element_text(size = 25))
perf <- read.delim("src/fare_count/perform_benchmark.tab")
perf$SizeLevel <- factor(perf$Size, sort(unique(perf$Size)),
                         format(sort(unique(perf$Size)), big.mark = ',', scientific = F))

p <- ggplot(data = perf, aes(x = SizeLevel, y = Seconds, fill = Scheme)) +
  geom_bar(position = 'dodge', stat="identity") +
  geom_text(aes(label = Seconds), position = position_dodge(width = .9),
            hjust = -0.05) +
  xlab('Amount of Tuples') + ylab('Time (s)') +
  ggtitle('In-Mapping Combiner v.s. Classic') +
  coord_flip() +
  myGthm

png(filename = file.path(getwd(), 'fig/Perf_InMapCombiner.png'), width = 1200, height = 700)
print(p)
dev.off()

pdf(file = file.path(getwd(), 'fig/Perf_InMapCombiner.pdf'), 12, 7)
print(p)
dev.off()
