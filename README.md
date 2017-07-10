# Movie Recommendation App

This Flask project will be done over the course of several weeks.

## The Concept

Rotten Tomatoes tells us the percentage of critics that received a "good" review.
https://www.rottentomatoes.com/about/

The challenge is that it is not personalized. Critic consensus does not always mean we will enjoy a movie.

Movies are subjective as are critics and individuals

What if there was an app that only showed us critics we personally agreed with?

## Part 1

Start small with a list of critics and whether they liked a movie.

Here we will find movie reviews to create a data model of critics, movie titles, and a 1 or 0 indicating if they liked the movie.

Since this is a prototype, we will limit our search to 2017 movies and reviews

## Part 2

Routes will be:

A table of movies reviewed.
A table of critics.
A table of the individual critic displaying the movies they reviewed and if they liked it.

## Part 3

Item to Item collaborative filtering. We will script this and hard code user input to test.
If a user says they liked movies x and y, this will output recommendations

## Part 4

User interface:
1.) The front end should display movies so the user can click which titles they liked
2.) A button will prompt for recommendations
3.) A page of movie recommendations is displayed
