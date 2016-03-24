source('plotARIMA.R')

plotValidation <- function(arima.model, current_x) {
    #arima.model: data frame, model produced by running forecast(arima)
    #current_x: time series, values that correspond to arima.model$x but for
    #                        current time period. Used to overlay actual data
    #                        on model forecast.
    #plots arima forecast with true data overlayed on the forecast region

    validation.length <- length(arima.model$x)
    current.dates <- as.POSIXlt(index(as.xts(current_x)))[(validation.length+1):
                                                          length(current_x)]
    current.vals <- as.numeric(current_x)[(validation.length+1):
                                          length(current_x)]
    current.df <- data.frame(dates=current.dates, vals=current.vals)

    plot.arima <- plotARIMA(arima.model)

    if (any(current.df$vals > arima.model$upper[, '95%']) ||
        any(current.df$vals < arima.model$lower[, '95%'])) {
        color = 'red'
    }
    else {
        color = 'blue'
    }

    plot.arima <- plot.arima + geom_line(data=current.df, aes(x=dates, y=vals),
                                         color=color)
    return(plot.arima)
}