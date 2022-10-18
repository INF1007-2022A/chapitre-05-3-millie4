#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	letter_num = 0
	for i in text:
		if i.isalnum():
			letter_num += 1
	return letter_num

def get_word_length_histogram(text):
	mots = []
	for n in text.split():
		mots.append(get_num_letters(n))
	histogramme = []
	word_length = 0
	while sum(histogramme) < len(mots):
		histogramme.append(0)
		for n in range(len(mots)):
			if word_length == mots[n]: histogramme[word_length] += 1
		word_length += 1
	return histogramme

def format_histogram(histogram):
	result = ""
	for i in range(1,len(histogram)):
		stars = "*" * histogram[i]
		decalage = len(str(len(histogram)-1)) ## pk??
		result += f"{i:>{decalage}} {stars} \n"
	return result

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	axe = LINE_CHAR * (len(histogram)-1)
	result = ""
	for j in range(max(histogram)):
		for i in range(1,len(histogram)):
			if histogram[i] >= max(histogram) - j:
				result += BLOCK_CHAR
			else: result += " "
		result += "\n"
	result += axe
	return result

if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	print(get_num_letters(spam))
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
