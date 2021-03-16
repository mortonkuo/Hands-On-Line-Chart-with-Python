# Hands-On-Line-Chart-with-Python
**Drawing a satisfactory line chart by matplotlib.pyplot**

- Same article on Medium: https://medium.com/analytics-vidhya/ml11-16baa318c73b

- Visualization always comes first when it comes to ML/DS project. Visualization help get insights of a given dataset, and through EDA (exploratory data analysis) we rely on visualization and other manners to prepare for building a performant model.

- This data is the word counts of FOMC minutes from 1993/01 ~ 2020/09 after data selection and data pre-processing (by me), along with the Fed fund rate change after each FOMC. FOMC minute is released 3 weeks after every FOMC meeting. The data sources come from FOMC minutes & FOMC’s target federal funds rate or range, change (basis points) and level.

## Outline
(1) Importance of Visualization in a ML/DS Project \
(2) Our goal: A Real-World Case \
(3) Starting Point: A Primitive Line Chart \
(4) High Definition & Tight Layout \
(5) Figure size & Font Size \
(6) Axis & Type of Line and Marker \
(7) Grid \
(8) More Info: Shadow \
(9) More Info: Annotation \
(10) More Info: Up, Down or Unchanged \
(11) Reference \


## (1) Importance of Visualization in a ML/DS Project

> … that very different Machine Learning algorithms, including fairly simple ones, performed almost identically well on a complex problem of natural language disambiguation once they were given enough data. [1]

There are a couple of main challenges of machine learning as follows: [1]
1. Insufficient Quantity of Training Data
2. Nonrepresentative Training Data
3.  Poor-Quality Data
4.  Irrelevant Features
5.  Overfitting the Training Data
6.  Underfitting the Training Data

Figure 1: Peformances of algorithms given enough data

> In a famous paper published in 2001, Microsoft researchers Michele Banko and Eric Brill showed that very different Machine Learning algorithms, including fairly simple ones, performed almost identically well on a complex problem of natural language disambiguation once they were given enough data (as you can see in Figure 1).
As the authors put it: “these results suggest that we may want to reconsider the tradeoff between spending time and money on algorithm development versus spending it on corpus development.” \
> The idea that data matters more than algorithms for complex problems was further popularized by Peter Norvig et al. in a paper titled “The Unreasonable Effectiveness of Data” published in 2009.10 It should be noted, however, that small- and mediumsized datasets are still very common, and it is not always easy or cheap to get extra training data, so don’t abandon algorithms just yet. \
> It should be noted, however, that small- and medium- sized datasets are still very common, and it is not always easy or cheap to get extra training data, so don’t abandon algorithms just yet. [1]

Now that we see how major the sufficient quantity of data can impact a ML/DS project, it’s a not a surprise that the other challenges like “Nonrepresentative Training Data”, “Poor-Quality Data”, “Irrelevant Features” may significantly affect the performance of a ML/DS project. \

So, visualization is the right tool to help solve those three challenges — “Nonrepresentative Training Data”, “Poor-Quality Data”, “Irrelevant Features.”


## (2) Our goal: A Real-World Case
Let’s go straight to a real-world case— the line chart we desire — then we would see how to build this satisfactory line chart from scratch. “Up”, “Down”, and “Unchanged” stand for the targeted Fed fund rate change after every FOMC meeting.

Figure 2: The desired line chart. It will appear again at the end of this article.


## (3) Starting Point: A Primitive Line Chart



Check matplotlib’s official document for more details (setting markers, colors) of matplotlib.pyplot.plot. Also, check the matplotlib’s official document for the complete list of named colors. Note that Pickle is a Python-specific data format.


## (4) High Definition & Tight Layout



## (5) Figure size & Font Size


The following annotations are noteworthy.

1. family: A list of font names in decreasing order of priority. The items may include a generic font family name, either 'serif', 'sans-serif', 'cursive', 'fantasy', or 'monospace'. In that case, the actual font to be used will be looked up from the associated rcParam. Try fontname = 'Comic Sans MS' & fontname="Arial".
2. fontsize: Either an relative value of 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' or an absolute font size, e.g., 12.

## (6) Axis & Type of Line and Marker


## (7) Grid


Then, let’s see what can we do to create extraordinary grid. Just adjust the line plt.grid( ).

Check matplotlib’s official document matplotlib.pyplot.grid.

## (8) More Info: Shadow


The light blue spans are recessions. Check US National Bureau of Economic Research & matplotlib.pyplot.axvspan.

## (9) More Info: Annotation

Check matplotlib.pyplot.annotate or Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython (2nd ed.).


## (10) More Info: Up, Down or Unchanged

“Up”, “Down”, and “Unchanged” stand for the targeted Fed fund rate change after every FOMC meeting.


Finally, here we see this satisfactory line chart again! We can compare it with the graph below.
