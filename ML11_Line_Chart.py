#%% (1) Introduction

# -*- coding: utf-8 -*-
"""
# ML11: Hands-On Line Chart by Python
# https://merscliche.medium.com/ml11-16baa318c73b
# @author: Morton Kuo (2020/12/10)
"""

'''
Pic, Data & Python Code: 
https://drive.google.com/drive/folders/1Haknut4yGujlWP-QKpJnFWwRJE1xtf9Y

This data are the word counts of FOMC minutes from 1993/01 ~ 2020/09 after data selection and data 
pre-processing (by me), along with the Fed fund rate change after each FOMC. FOMC minute is released 3 weeks 
after every FOMC meeting. The data sources come from FOMC minutes & FOMC's target federal funds rate 
or range, change (basis points) and level.
'''

#%% (2) Input & Setup
import os
os.chdir('D:\\G03_1\\Medium\\ML11') # Change it to desired directory
os.getcwd()

import pickle # Python-specific data format
with open("ML11_FOMC.pickle", 'rb') as file: # 'rb': read & binary
    ML11_Morton_Kuo = pickle.load(file)

import numpy as np
FOMC_words = np.array(ML11_Morton_Kuo[0])
up_index = np.array(ML11_Morton_Kuo[1])
down_index = np.array(ML11_Morton_Kuo[2])
unchanged_index = np.array(ML11_Morton_Kuo[3])

import matplotlib.pyplot as plt



#%% (3) Starting Point: A Primitive Line Chart
plt.figure(figsize=(18, 6))
plt.plot(list(range(1,223)), FOMC_words, 'bo') 
# Draw markers. 'b' is blue. 'o' is circle marker.
plt.plot(list(range(1,223)), FOMC_words, 'k')
# Draw a line. 'k' is black. No marker, the data will be a line without markers.

plt.xlabel('Ordinal number (1993 ~ 2020)')
plt.ylabel('Words')
plt.title('Words of FOMC minutes from 1993 to 2020')

plt.xticks(range(0, 224, 25))  
plt.yticks(range(0, 5001, 500))

plt.savefig('02_FOMC_Primitive.png') # 54.8 kb. Pretty small.
plt.close() # Close the current figure



#%% (4) High Definition & Tight Layout
plt.figure(figsize=(18, 6))
plt.plot(list(range(1,223)), FOMC_words, 'bo') 
plt.plot(list(range(1,223)), FOMC_words, 'k')


plt.xlabel('Ordinal number (1993 ~ 2020)')
plt.ylabel('Words')
plt.title('Words of FOMC minutes from 1993 to 2020')

plt.xticks(range(0, 224, 25))  
plt.yticks(range(0, 5001, 500))

plt.tight_layout() # tight layout for plt.show()
plt.savefig('03_FOMC_High_Definition_Tight_Layout.png', dpi= 800, bbox_inches= 'tight') 
# 1.17 MB. High definition. By default, dpi= 100. 
# bbox_inches= 'tight' makes to saved figure tight layout
plt.close() 



#%% (5) Figure Size & Font Size 
plt.figure(figsize=(15, 5)) # Change figure size
plt.plot(list(range(1,223)), FOMC_words, 'bo') 
plt.plot(list(range(1,223)), FOMC_words, 'k')

plt.xlabel('Ordinal number (1993 ~ 2020)', fontsize = 'xx-large') # Change font size
plt.ylabel('Words', fontsize = 'xx-large') # Change font size
plt.title('Words of FOMC minutes from 1993 to 2020', fontname='Comic Sans MS', fontsize = 'xx-large') # Change font size
'''
1. family: A list of font names in decreasing order of priority. The items may include a generic font family name, 
either 'serif', 'sans-serif', 'cursive', 'fantasy', or 'monospace'. In that case, the actual font to be used will 
be looked up from the associated rcParam. Try fontname = 'Comic Sans MS' & fontname="Arial".

2. fontsize: Either an relative value of 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' 
or an absolute font size, e.g., 12.
'''

plt.xticks(range(0, 224, 25))  
plt.yticks(range(0, 5001, 500))
plt.savefig('04_FOMC_Figure_Size_Font_Size.png', dpi= 800, bbox_inches= 'tight') 
plt.close() 



#%% (6) Axis & Type of Line and Marker
plt.figure(figsize=(15, 5)) 
plt.plot(list(range(1,223)), FOMC_words, 'p', color= 'royalblue') # Color changed
plt.plot(list(range(1,223)), FOMC_words, '--k') # Color changed

plt.xlabel('Ordinal number (1993 ~ 2020)', fontsize = 'xx-large') 
plt.ylabel('Words', fontsize = 'xx-large')
plt.title('Words of FOMC minutes from 1993 to 2020', fontname='Comic Sans MS', fontsize = 'xx-large') 

plt.axis([-1, 224, 0, 4800]) # Adjust the scope
plt.xticks(range(0, 224, 25))  
plt.yticks(range(0, 5001, 500))

plt.savefig('05_FOMC_Axis_Line_Type.png', dpi= 800, bbox_inches= 'tight') 
plt.close() 



#%% (7) Grid

## Grid_1
plt.figure(figsize=(15, 5)) 
plt.plot(list(range(1,223)), FOMC_words, 'p', color= 'royalblue') 
plt.plot(list(range(1,223)), FOMC_words, '--k')

plt.xlabel('Ordinal number (1993 ~ 2020)', fontsize = 'xx-large')
plt.ylabel('Words', fontsize = 'xx-large')
plt.title('Words of FOMC minutes from 1993 to 2020', fontname='Comic Sans MS', fontsize = 'xx-large') 

plt.axis([-1, 224, 0, 4800]) 
plt.xticks(range(0, 224, 25))  
plt.yticks(range(0, 5001, 500))
plt.grid() # Simply add grid by default

plt.savefig('06_FOMC_Grid_1.png', dpi= 800, bbox_inches= 'tight') 
plt.close() 


## Grid_2
plt.figure(figsize=(15, 5)) 
plt.plot(list(range(1,223)), FOMC_words, 'p', color= 'royalblue') 
plt.plot(list(range(1,223)), FOMC_words, '--k')

plt.xlabel('Ordinal number (1993 ~ 2020)', fontsize = 'xx-large') 
plt.ylabel('Words', fontsize = 'xx-large') 
plt.title('Words of FOMC minutes from 1993 to 2020', fontname='Comic Sans MS', fontsize = 'xx-large') 

plt.axis([-1, 224, 0, 4800]) 
plt.xticks(range(0, 224, 25))  
plt.yticks(range(0, 5001, 500))
plt.grid(color='slategray', linestyle='-.', linewidth= 1.2, b=None, which='major', axis='both')
# Try to adjust color, linestyl, and linewidth. By default, linestyle= '-', linewidth= 1. 
# The default of color is not indicated by the official document; however, it is close to 'silver'.

plt.savefig('07_FOMC_Grid_2.png', dpi= 800, bbox_inches= 'tight') 
plt.close() 



#%% (8) More Info: Shadow

plt.figure(figsize=(15, 5)) 
plt.plot(list(range(1,223)), FOMC_words, 'p', color= 'royalblue') 
plt.plot(list(range(1,223)), FOMC_words, '--k')

plt.xlabel('Ordinal number (1993 ~ 2020)', fontsize = 'xx-large')
plt.ylabel('Words', fontsize = 'xx-large')
plt.title('Words of FOMC minutes from 1993 to 2020', fontname='Comic Sans MS', fontsize = 'xx-large') 

plt.axis([-1, 224, 0, 4800]) 
plt.xticks(range(0, 224, 25))  
plt.yticks(range(0, 5001, 500))
plt.grid() 

# Shadow
plt.axvspan(66, 71, color='lightblue', alpha=0.5, lw=0)
plt.axvspan(120, 132, color='lightblue', alpha=0.5, lw=0)
plt.axvspan(218, 222, color='lightblue', alpha=0.5, lw=0)

plt.savefig('08_FOMC_Shadow.png', dpi= 1000, bbox_inches= 'tight') # dpi: 800 -> 1000
plt.close() 



#%% (9) More Info: Annotation

plt.figure(figsize=(15, 5)) 
plt.plot(list(range(1,223)), FOMC_words, 'p', color= 'royalblue') 
plt.plot(list(range(1,223)), FOMC_words, '--k')

plt.xlabel('Ordinal number (1993 ~ 2020)', fontsize = 'xx-large')
plt.ylabel('Words', fontsize = 'xx-large')
plt.title('Words of FOMC minutes from 1993 to 2020', fontname='Comic Sans MS', fontsize = 'xx-large') 

plt.axis([-1, 224, 0, 4800]) 
plt.xticks(range(0, 224, 25))  
plt.yticks(range(0, 5001, 500))
plt.grid() 

plt.axvspan(66, 71, color='lightblue', alpha=0.5, lw=0)
plt.axvspan(120, 132, color='lightblue', alpha=0.5, lw=0)
plt.axvspan(218, 222, color='lightblue', alpha=0.5, lw=0)

# Annotation 
crisis_data = [
    (66, '2001/03. Peak. Dot-Com Bubble.'),
    (120, '2007/12. Peak. Financial Crisis.'),
    (218, '2020/02. Peak. COVID-19.')]

x, label = crisis_data[0]
plt.annotate(label, xy=(x, FOMC_words[x] - 600),
             xytext= (x, FOMC_words[x] - 1200),
             arrowprops= dict(facecolor='black', headwidth= 4, width=2, headlength= 4),
             horizontalalignment='left', verticalalignment= 'top', fontsize = 'x-large')

x, label = crisis_data[1]
plt.annotate(label, xy=(x, FOMC_words[x] - 1000),
             xytext= (x, FOMC_words[x] - 1600),
             arrowprops= dict(facecolor='black', headwidth= 4, width=2, headlength= 4),
             horizontalalignment='left', verticalalignment= 'top', fontsize = 'x-large')

x, label = crisis_data[2]
plt.annotate(label, xy=(x, FOMC_words[x] - 1200),
             xytext= (x, FOMC_words[x] - 1700),
             arrowprops= dict(facecolor='black', headwidth= 4, width=2, headlength= 4),
             horizontalalignment='right', verticalalignment= 'top', fontsize = 'x-large')


plt.savefig('09_FOMC_Annotation.png', dpi= 1000, bbox_inches= 'tight') 
plt.close() 



#%% (10) More Info: Up, Down or Unchanged

plt.figure(figsize=(15, 5)) 

plt.plot(up_index+1 ,  FOMC_words[up_index], 'o', color= 'blue', label="Up")  # up_index 
plt.plot(down_index+1,  FOMC_words[down_index], 's', color= 'orangered', label="Down")  # down_index 
plt.plot(unchanged_index+1,  FOMC_words[unchanged_index], '*', color= 'darkgreen', label="Unchanged")  # unchanged_index 
# Draw 3 kinds of markers and change their colors.
# 'o' is circle marker;'s' is square marker; '*' star marker. 
# Add labels and plt.legend() will catch them later 
plt.plot(list(range(1,223)), FOMC_words, '--k')

plt.xlabel('Ordinal number (1993 ~ 2020)', fontsize = 'xx-large')
plt.ylabel('Words', fontsize = 'xx-large')
plt.title('Words of FOMC minutes from 1993 to 2020', fontsize = 'xx-large') 

plt.axis([-1, 224, 0, 4800]) 
plt.xticks(range(0, 224, 25))  
plt.yticks(range(0, 5001, 500))
plt.grid() 

plt.axvspan(66, 71, color='lightblue', alpha=0.5, lw=0)
plt.axvspan(120, 132, color='lightblue', alpha=0.5, lw=0)
plt.axvspan(218, 222, color='lightblue', alpha=0.5, lw=0)

crisis_data = [
    (66, '2001/03. Peak. Dot-Com Bubble.'),
    (120, '2007/12. Peak. Financial Crisis.'),
    (218, '2020/02. Peak. COVID-19.')]

x, label = crisis_data[0]
plt.annotate(label, xy=(x, FOMC_words[x] - 600),
             xytext= (x, FOMC_words[x] - 1200),
             arrowprops= dict(facecolor='black', headwidth= 4, width=2, headlength= 4),
             horizontalalignment='left', verticalalignment= 'top', fontsize = 'x-large')

x, label = crisis_data[1]
plt.annotate(label, xy=(x, FOMC_words[x] - 1000),
             xytext= (x, FOMC_words[x] - 1600),
             arrowprops= dict(facecolor='black', headwidth= 4, width=2, headlength= 4),
             horizontalalignment='left', verticalalignment= 'top', fontsize = 'x-large')

x, label = crisis_data[2]
plt.annotate(label, xy=(x, FOMC_words[x] - 1200),
             xytext= (x, FOMC_words[x] - 1700),
             arrowprops= dict(facecolor='black', headwidth= 4, width=2, headlength= 4),
             horizontalalignment='right', verticalalignment= 'top', fontsize = 'x-large')


plt.legend(fontsize = 'large') # Indicate the labed markers
'''
1. fontsize: Either an relative value of 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' 
or an absolute font size, e.g., 12.
'''
plt.savefig('10_FOMC_Up_Down_Unchanged.png', dpi= 1000, bbox_inches= 'tight') 
plt.close() 
