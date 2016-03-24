library(xts)

plotARIMA <- function(arima.model, plot.mean=FALSE) {
    #arima.model: data frame, model produced by running forecast(arima)
    #plot.mean: boolean, whether to plot the mean of the prediction forecast.
    #                    defaults to FALSE
    #plots the arima forecast

    data.dates <- as.POSIXlt(index(as.xts(arima.model$x)))
    data.vals <- as.numeric(arima.model$x)
    data.df <- data.frame(dates=data.dates, vals=data.vals)

    forecast.dates <- as.POSIXlt(index(as.xts(arima.model$mean)))
    forecast.df <- data.frame(dates=forecast.dates,
                              mean=arima.model$mean,
                              upper=arima.model$upper[, '95%'],
                              lower=arima.model$lower[, '95%'])

    plot <- ggplot(data.df) + geom_line(aes(x=dates, y=vals)) +
            ggtitle(paste('Forecasts from', arima.model$method)) + theme_bw() +
            geom_ribbon(data=forecast.df, aes(x=dates, ymin=lower, ymax=upper),
                        color='lightgray', fill='lightgray') +
            xlab('Date') + ylab('Basses')
    if (plot.mean){
        plot <- plot + geom_line(data=forecast.df, aes(x=dates, y=mean),
                                 color='darkgreen', linetype='dashed')
    }
    return(plot)
}