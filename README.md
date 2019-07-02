# recommender-system
A recommender system using item CF built with Hadoop framework.
This model contains five mapReduce jobs.

Raw data: userId, movieId, rating.
(The raw data used in the model is provided by https://www.jiuzhang.com.)

# structures
## DataDividedByUser
Merge data for each user.

userId, movieId, rating --> userId \t movie1:rating1,movie2,rating2...(ratings of movies watched by each user)

## CoOcurrenceMatrixGenerator
Count the times two movies occur in the same user's list. Build coocurrence matrix based on the raw data.

Mapper: userid \t movie1: rating, movie2: rating... --> movie1: movie2 \t value = 1 ...

Reducer: movie1: movie2 \t <1, 1, 1, 1 ...> --> movie1:movie2 \t 20 ...(calculate each two movies have been watched by how many people)

## Normalized
Collection the relationships for each movie and normalize each unit of co-occurrence matrix.

Notice that the normalized relationship of (movie1,movie2) and (movie2,moive1) are different.

## Multiplication
Split matrix multiplication into multiplication of tiny cells of the matrixs.

output: user1:movie1 \t m11 * r11, user1:movie1 \t m13 * r31, ...

|   |m1  |m2  |m3  |m4  |       
|---|:--:|---:|:--:|---:|
|m1 |m11 |m12 |m13 |m14 |
|m2 |m21 |m22 |m23 |m24 |
|m3 |m31 |m32 |m33 |m34 |
|m4 |m41 |m42 |m43 |m45 |

Here the matrix of users and moives are get from the processed data. There might be moives which a certain user didn't rate. In this case, pad the empty with the average rating value of the user.

|   |u1  |u2  |
|---|:--:|---:|
|m1 |r11 |r12 |
|m2 |r21 |r22 |
|m3 |r31 |r32 |
|m4 |r41 |r42 |

## Sum
Collect and add up user:movie pairs.

output: user1:movie1 \t m11 * r11 + m12 * r21 + m13 * r31 + m14 * r41


