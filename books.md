Post
====

I was listening to an old episode of [Partially
Derivative](http://www.partiallyderivative.com/), a podcast on data
science and the news. One of the hosts mentioned that we're now living
in the "golden age of data science instruction" and learning materials.
I couldn't agree more with this statement. Each month, most publishers
seem to have another book on the subject and people are writing exciting
blog posts about what they're learning and doing.

I wanted to outline a few of the books that helped me along the way, in
the order I approached them. Hopefully, you can use them to gain a
broader perspective of the field and perhaps as a resource to pass on to
others trying to learn.

[Learning from Data](http://www.amazon.com/Data-Science-Business-data-analytic-thinking/dp/1449361323)
------------------------------------------------------------------------------------------------------

I first found Learning from Data through Caltech's
[course](http://work.caltech.edu/telecourse.html) on the subject. I
still think it's an excellent text but I'm not sure if I would recommend
it to the absolute beginner. (To someone who is just coming to the
subject, I would probably recommend the next choice down on the list.)

However, if you have a little bit of background in linear algebra and
probability (enough to be able to read the notation and look up what
things mean should be fine) then it is absolutely a great book to read
for getting started. Learning from Data gave me a first taste that
there's some rigorous mathematical theory behind a lot of the algorithms
employed in data science. If working with data and seeing results shows
you that these methods work, the theory tells you **why** it works.

Now, understanding a few things about the theory is great, but most of
the time, people want to know what it can actually **do**.

[Data Mining Techniques: For Marketing, Sales, and Customer Relationship Management](http://www.amazon.com/Data-Mining-Techniques-Relationship-Management/dp/0470650931)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I'll admit to only having had a cursory understanding of what was
possible before I read Data Mining Techniques. I knew that the most
widely used algorithms were used for assessing risk, like credit scores.
However, I didn't know much about how you could make gains in the world
of marketing using data science techniques.

I appreciated that the authors have a lot of experience in the field,
especially experience that predates most of the growth in big data these
days. This book makes it clear that many of the most useful algorithms
have been around and in use for decades. The authors also offer some
explanations from the direct marketing case (print magazines and
physical mail) that I hadn't considered, such as ranking algorithms,
which were originally used to prioritize a list of people to contact
because of the high costs of mailing paper to people.

More than anything, I liked the breadth of the topics, since they cover
just about every form of marketing algorithm and do a great job of
giving you a high level view of why they matter.

You won't walk away from this book knowing how to implementing
everything they talk about, but you will get a sense for which
algorithms are suited for particular tasks.

This book gave me a better way to think through the initial phases of a
project, but I still needed some help in learning how to communicate
about data and how to fit it directly into the business context.

[Data Science for Business](http://www.amazon.com/Data-Science-Business-data-analytic-thinking/dp/1449361323)
-------------------------------------------------------------------------------------------------------------

I read through this one while I was on vacation (yes, I know, I'm that
type of geek). That didn't stop me from soaking up a lot of information
from it about how data science applies to a company trying to use these
models. Most of the book is focused on helping you think through how to
operationalize the process of running and managing a data science
project and what outcomes you might expect from the effort.

Beyond that, I think it taught me how to communicate better about data
at a company. Being able to talk about the many months it will take to
bring a project into fruition and weigh it against
[alternatives](http://saedsayad.com/oner.htm) is the bread and butter of
working at a company that wants to make money. Moreover, if you believe
that a particular project is the right choice, you need to be able to
back up that choice by communicating about the benefits.

I want to say that this is a very "bottom-line" type of book, but that's
okay to hear about some of the time. Data science doesn't always have to
be about the hottest technique or the biggest technology if your
priorities include keeping your costs below your revenue. However, I
still didn't learn much about getting my hands dirty with the data on a
day-to-day basis. For that, I had to rely on the final book I present.

[Applied Predictive Modeling](http://www.amazon.com/Applied-Predictive-Modeling-Max-Kuhn/dp/1461468485)
-------------------------------------------------------------------------------------------------------

This is a book on predictive modeling in R and on using [a
package](https://topepo.github.io/caret/index.html) that the author
developed for doing that. Overall, I think that even if you don't end up
using R as your go-to tool for analyzing data, you'll still learn a lot
from this book. It thoroughly demonstrates the power caret can offer you
in a project, to the point that you'll seek the same functionality in
your tool of choice (or hopefully build its equivalent for us).

As a software tool, caret offers a consistent interface for just about
any predictive task (classification or regression) that you could ask
for. One issue some people have with R packages is that the interface
for algorithms isn't very consistent. Learning how to use one package
won't always lead to the same understanding in a completely different
package. Caret addresses that by giving you the same way to set up a
modeling task for [many different
algorithms](https://topepo.github.io/caret/modelList.html). Moreover, it
also automates several tasks like:

-   Data splitting into training and test sets
-   Data transformations like normalization or power transforms
-   Modeling tuning and parameter selection

Essentially, it makes working in R a lot like using [Scikit
Learn](http://scikit-learn.org/) but with many more options and model
implementations.

So that's all you need, right? Just read a couple of books and you're on
your way? Not quite. You'll actually have to apply some of this and
learn from it. Perhaps next time you're in a meeting discussing
priorities for your company, you will need to frame the conversation
about your next data project and directing the data effort toward your
business goals ([Data Science for
Business](http://www.amazon.com/Data-Science-Business-data-analytic-thinking/dp/1449361323)).
When you're brainstorming possible things that you could try to predict
and use in a marketing campaign, you will need to outline the possible
techniques and what they could offer you ([Data Mining
Techniques](http://www.amazon.com/Data-Mining-Techniques-Relationship-Management/dp/0470650931)).
If you're evaluating candidate algorithms for their ability to perform
the task accurately, you will need to gauge their effectiveness from a
theoretical ([Learning from
Data](http://www.amazon.com/Data-Mining-Techniques-Relationship-Management/dp/0470650931))
and practical ([Applied Predictive
Modeling](http://www.amazon.com/Applied-Predictive-Modeling-Max-Kuhn/dp/1461468485))
standpoint.

I hope this helps you apply data science at work and gives you
perspective in the field.
