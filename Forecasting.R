amtrak <- read.csv("Amtrak.csv")
 
ridership <- ts(amtrak$Ridership, start = c(1991,1),
                end = c(2004,3), freq=12)


plot(ridership, xlab="Time",ylab="Ridership", ylim=c(1300,2300), bty = "l")

#install.packages("forecast")
library(forecast)
ridership.lm <- tslm(ridership ~ trend + I(trend^2))

par(mfrow = c(2,1))
plot(ridership, xlab="Time", ylab="Ridership",
     ylim=c(1300,2300), bty="l")
lines(ridership.lm$fitted, lwd=2)


ridership.zoom <- window(ridership, start=c(1997,1),
                         end=c(2000,12))
plot(ridership.zoom, xlab="Time", ylab="Ridership",
     ylim=c(1300,2300), bty="l")

ridership.zoom
