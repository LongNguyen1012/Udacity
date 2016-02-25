## Summary
Using Prosper loan data, I visualize the risk and return trade off of various types of Prosper loan and comapre them with some of the most popular mutual funds in the market. 

Risk of each type of Prosper loan is the average of its estimated loss, whie return is the average of its estimated effective yield. For mutual funds, standard deviation is used to measure risk, and total return is used to measure return over each period.

The darker the color hue, the higher the Sharpe ratio of the portfolio.

## Design
Initially, I have two charts on my page, one displaying the risk/return trade off; the other one shows how many loans of each term are in each specific rating category. The first chart is a scatter plot, while the second chart is a combination of scatter plot and pie charts. In the second chart, scatter plot shows the risk/return of each type of Prosper loan, while the pie chart shows how many of each types are 12, 36, and 60 months term. However, after collecting feedback, I realized that the second chart is redundant, and decided to update only one the first chart. Thus, the new chart not only displays scatter plots, but also tool tips to show the details of each portfolio, separate colors to distiguish between Prosper loans and other portfolios, and color hue to show the magniutde of Sharpe ratio. 

## Feedback

###yan_24332845395244373d: 

What do you notice in the visualization?
I see return/risk ratings for various Prosper loans, as well as for several conventional investment choices.

What questions do you have about the data?
Not clear what units for the return and risk ratings.

What relationships do you notice?
Return and risk seem positively correlate: higher return is associated with higher risk.

What do you think is the main takeaway from this visualization?
Some Prosper investments are better than those listed conventional investment, because the Prospers carry same risks but offer better return.

Is there something you don’t understand in the graphic?
Choice of colors for various Prospers don't seem so clear to me. Are they diverging colors?


###yavigol3d:

What do you notice in the visualization?
* (Chart1): Risk for the funds is usually higher than for prosper loans for the same return level
* (Chart2): Term structure of loans by Prosper rating
* (Chart2): For all Prosper ratings, 3-year term loans have largest share with 5- and 1-year loans being second and third by the share

What questions do you have about the data?

(Chart1): It is not clear why there is no information on funds when 1-year option selected
(Chart1, 2): What time the data relates to?
What relationships do you notice?

(Chart1): Higher risk Prosper loans generate higher returns
(Chart2): For all Prosper ratings, 3-year term loans have largest share with 5- and 1-year loans being second and third by the share
What do you think is the main takeaway from this visualization?

Prosper loans are relatively less risky than funds
Higher risk loans typically generate higher returns
Is there something you don’t understand in the graphic?
Everything is quite clear

Some suggestions
Chart1

I would put a header to this chart
It is also possible to create tooltips showing risk and return values for each circle
Finance theory says that return depends on risk. Therefore it can be better to plot return along y axis and risk - along x axis
When 3 year loans are selected, MSIQX circle is located to the left from y axis and, therefore, covers the axis value. It can be a good idea to move y axis to the left so the circle gets to the right side from the axis
You can also segregate Prosper related circles from other funds visually (e.g. same fill or line color)
You can indicate somewhere what time period the data relates to
Label values can be converted from decimal to % format
Chart2

Information on return vs. risk is reflected on the first chart already. It can be better to focus on the term structure part of the data here and to use some other chart type (e.g. bar charts) to show the structure
I would put a header to this chart
I would show color coding in a legend box separately and would leave only numerical values in tooltips


###chris_286663:

Hi Long,

I want to give you some overall feedback since the last two reviews focused specifically on the questions asked. I think this might help in making the visualization easier for the casual reader (rather than the informed reader) since I'm not familiar with the prosper loan data set.

First, I think it might help to add an additional sentence on what a prosper loan is. I could guess from the chart but I'm not exactly sure.

Initially, it isn't apparent that there are buttons on the left until I do some exploring. Maybe add some kind of styling so that it is more clear that they are buttons to facet the chart.

I think it also might help to add a legend on the right of the first chart as well. It seems to me that you are comparing prosper loans to some mutual funds. Maybe color each prosper loan individually and have one color for all other mutual funds even though there are several in the chart. Hovering over each mutual fund will give detailed info if the viewer wants more. This would give more emphasis to those prosper loans.

There is one mutual fund that has a negative return in the first chart that goes off the x-axis. Maybe extend the x-axis to include a negative range so that it doesn't go off the chart.

On the second chart I was at first unsure of what is being communicated after reading. Because position (X, Y) is one of the primary ways people perceive information, my initial thought is that we are looking at the correlation between risk and return. It seems from the description that we might be focusing more on the number of loans in each category? If so the second chart seems a little redundant to the first. Maybe change the visual representation to emphasize that you want to focus on the number of loans in each category across term duration.

I hope this helps! Great job on your first iteration!

## Resources
https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.eventArgs
https://github.com/mbostock/d3/wiki/Transitions
http://stackoverflow.com/questions/24989128/why-is-my-d3-tip-not-working
https://www.udacity.com/course/viewer#!/c-ud507-nd/l-3069149263/m-3071138983
