#!/usr/bin/env python
# coding: utf-8
#take user input to generate a bar graph in Unicode using these characters:
# Box Drawing (lines on side)
linvert = ('┃','┨')
linhorz = ['━','┯')
lincorn = ('┗','╄')
# Lower n Quarters/Eighths Block (and Lower Half Block)
eighths = ('▁','▂','▃','▄','▅','▆','▇')
# Full Block
fullblk = '█'



#values = {"A":14.5,"bart":33,"cart":2}
#values = {"A":(14.5,0),"bart":(33,1),"cart":(2,2)}
#precision: set to number of sig figs you want to keep in the data, 1≤x≤8
#labels: set to 1 to force a key, it will use a key if any label is >3 chars
def graph (values, precision=1, labels=false):
    if labels=false:
        for x in values.keys():
            if len(x)>3:
                labels=true
    fraction=[]
    for x in values.keys:
        values[x] = round(x,precision)
        fraction.append((values[x]


def round(value, sigfig): #to scientific notation in tuple (float,scale)
    #I can't wrap my head around rounding for now. returns tuple of float and exponent.



#title is the scale of the graph. This feature is finished
def title (scale):
    prefix = ('','ten','hundred')
    numtype = ('',' thousand',' million',' billion',' trillion',' quadrillion',' quintillion')
    if scale == 0:
        scalestr = "ones"
    elif scale > 0:
        scalestr = prefix[abs(scale)%3]+numtype[abs(scale)//3]+"s"
    else:
        scalestr = prefix[abs(scale)%3]+numtype[abs(scale)//3]+"ths"
    return "scale: "+scalestr+" ("+scinote(scale)+")"

def scinote(scale): #int, scientific notation (10 to the power of scale)
    powers = "⁰¹²³⁴⁵⁶⁷⁸⁹⁻"
    normal = "0123456789-"
    exp = "10"
    for x in str(scale):
        exp += powers[normal.find(x)] #this replaces number with superscript
    return exp
