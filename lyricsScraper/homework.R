library(tidyverse)
library(tidytext)
#### QUESTİON 1 ####
# PART A
data <- read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-01-18/chocolate.csv")
head(data, 3)
# PART B
data %>% 
  unnest_tokens(word, most_memorable_characteristics) %>% 
  count(word, sort = TRUE)
# PART C
data <- data %>% 
  mutate_if(is.character, as.factor)
# PART D
data %>% 
  group_by(company_location) %>% 
  summarize(
    mean = mean(rating, na.rm = TRUE),
    sd = sd(rating, na.rm = TRUE),
    median = median(rating, na.rm = TRUE)
  ) %>% 
  head(8)

#### QUESTİON 2 ####
#PART A
library(ggplot2)
library(dplyr)
econ <- read.csv("econ.csv")
ggplot(econ, aes(x = CPI, y = HDI, color = Region)) +
  geom_point() +
  scale_color_manual(values = c("#FF2D00", "#0036FF", "#0800FF", "#FFE800", "#FF00FF","#00FFFB")) +
  labs(x = "Corruption Perception Index (CPI)", y = "Human Development Index (HDI)", title = "Relationship Between Corruption and Human Development") +
  theme_light()
#PART B
ggplot(econ, aes(x = CPI, y = HDI)) +
  geom_point() +
  facet_wrap(~ Region, ncol = 2) +
  labs(x = "Corruption Perception Index (CPI)", y = "Human Development Index (HDI)", title = "Relationship Between Corruption and Human Development") +
  theme_light()
#PART C
econ$Category <- cut(econ$HDI.Rank, 
                     breaks = c(-Inf, 40, 80, 120, 160, Inf), 
                     labels = c("Low", "Lower-Middle", "Middle", "Upper-Middle", "High"), 
                     include.lowest = TRUE)
#PART D
category_counts <- econ %>% 
  group_by(Category) %>% 
  summarise(count = n())
ggplot(category_counts, aes(x = count, y = Category, fill = Category)) +
  geom_bar(stat = "identity", show.legend = FALSE, color="black",fill="orange") +
  geom_text(aes(label = count), vjust = 0)+
  labs(x = "Count", y = "HDI Rank Categories", title = "Number of cases for each HDI rank category") +
  theme_minimal() 

#### QUESTİON 3 ####
#PART A
episodes <- read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-01-24/episodes.csv")
head(episodes)
#PART B
sapply(episodes, function(x) sum(is.na(x)))
#PART C
tapply(episodes$imdb_rating, episodes$season, function(x) mean(x[!is.na(x)]))
#PART D
apply(episodes[,c("viewers", "imdb_rating", "n_ratings")], MARGIN=2, function(x) sd(x, na.rm = TRUE))
