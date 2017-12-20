# Bayes' Theorem is the FuzzBuzz of Data Science

The other day, I did a technical interview that involved applying Bayes' Theorem to a simple example. It stumped me.  And it left me feeling empathy for folks who have had trouble with the FizzBuzz interview question.

## It doesn't reflect day-to-day work

FizzBuzz depends on understanding a few concepts, like conditional execution, the modulus operator, divisibility of numbers, and common denominators.Every programmer should be familiar with the modulus operator and it's relationship to divisibility, but knowing about it doesn't mean it's part of your bread and butter. The day-to-day of software engineering usually takes place at th higher level of understanding good design patterns, parsing requirements, and using APIs for their team's platform or framework. Diving down to a lower level to reproduce divisibility from simple mathematics is a shift in perspective and takes several mental cycles to get right if it's out of practice.

## It's stressful to problem solve on the spot

Unless you're made of steel, you'll probably get some form of jitters during an interview and this can hurt the way you solve problems.

In 2005, Beilock & Carr published a paper on performance of  math problems between high working-memory and low working-memory undergraduate students. The HWM group, which performed very well on simple mathematical problems at baseline, low-stress conditions performed significantly poorly in a high stress. (Incidentally, Beilock & Carr's experiment used a modular arithmetic task in their experiment, the same concept that is integral to FizzBuzz.)

Add the stress of trying to explain your solution to an interviewer and this is a recipe for a meltdown.

## Experience teases out edge cases, but experience fades with time

One of the really tricky parts about FizzBuzz is that is involves an edge case that can trip people up. Namely, when the number is 15, it's possible to print out all three of "Fizz," "Buzz," and "FizzBuzz" if you're not careful.

The problem with this is that edge cases aren't over-arching principles or theoretical concepts, they're anomalies. And people learn how to deal with anomalies by experiencing them. At work, edge cases would get discovered in a handful of ways, but most likely being a) a developer on the team has come across it before and b) there's a deliberate, likely time-consuming effort to enumerate possible cases to test them out. As I've mentioned above, case (a) isn't very likely because the edge cases of FizzBuzz aren't top-of-mind, and case (b) presents problems because of the stress of interviewing.
Bayes' Theorem

Bayes' Theorem (or Bayes' Rule) is just tricky enough behave like FizzBuzz in these situations. It's certainly something that every data scientist should know, but it isn't something he or she would use every day. It's complicated enough to be relegated to the class of abstract math problems, which take a hit during stressful situations. And finally, for edge cases in applying Bayes' Theorem (like whether two events are independent), it's difficult and unlikely for individuals to come up with suitable examples to test immediately.
