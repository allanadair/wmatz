wmatz
=====
This repository serves only as an example methodology for calculating the
weighted geometric median of 3D points.

Background
----------
For a recent project I was asked to write some software to calculate weighted
median centers for sets of related 3D points. There are several definitions that
can be used to define exactly what median center means, and here
I am sharing a method known as the center of minimum aggregate travel.

From `Wikipedia <https://en.wikipedia.org/wiki/Center_of_population>`_:

    *The geometric median is the point to which the population has the smallest
    possible sum of distances (or equivalently, the smallest average distance).
    Because of this property, it is also known as the point of minimum aggregate
    travel. Unfortunately, there is no direct closed-form expression for the
    geometric median; it is typically computed using iterative methods.*

For sample data and a better explanation of the process, I searched the online
textbook `Geospatial Analysis Online <http://www.spatialanalysisonline.com/>`_
to find a section covering `centroids and centers
<http://www.spatialanalysisonline.com/HTML/index.html?centroids_and_centers.htm>`_.

Sample data
-----------
Below is a table representing data borrowed from the Geospatial Analysis Online
textbook that has been slightly modified for testing and verification purposes.

+------+------+------+-----+--------+
| Name | X    | Y    | Z   | Weight |
+======+======+======+=====+========+
| A    | 3.0  | 0.0  | 0.0 | 1.0    |
+------+------+------+-----+--------+
| B    | 14.0 | 3.0  | 0.0 | 1.0    |
+------+------+------+-----+--------+
| C    | 10.0 | 4.0  | 0.0 | 1.0    |
+------+------+------+-----+--------+
| D    | 13.0 | 11.0 | 0.0 | 1.0    |
+------+------+------+-----+--------+
| E    | 4.0  | 13.0 | 0.0 | 1.0    |
+------+------+------+-----+--------+
| F    | 0.0  | 8.0  | 0.0 | 1.0    |
+------+------+------+-----+--------+

The textbook data is actually 2D and unweighted, but we can add a third dimension
and set all weights to 1 to use the data for verification.

See the unit test for an example.
