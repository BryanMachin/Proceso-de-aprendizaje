# LearnPro: Learning Process Simulator

Learning a subject can pose a difficulty for a student when faced with a set of contents whose nature is completely unknown. For this reason, optimizing a learning process is a job that would present great difficulties. This work proposes an alternative solution to this problem.

LearnPro application is designed to provide the user with easy management of system specifications, making use of the Streamlit framework.

## Prerequisites for Streamlit Installation:
-	Python 3.9
-	PIP

## Streamlit Installation:
  At the Windows Command Prompt type:
  -	pip install streamlit
  -	pip install graphviz
  -	pip install streamlit-option-menu

To test that the application was installed correctly, write below:
  -	streamlit hello

To run the application, you must open a terminal within the folder where the project is located and write the following:
  -	streamlit run learnProApp.py

As soon as you run the above script, a local Streamlit server will be activated and the application will open in a new tab of the default web browser. As you can see, the application consists of a main module that contains a code editor for the learnPro language, and an output console at the bottom.

On the left is a sidebar that contains the Main Menu of the application. The "View Result" option makes it easy to view LearnPro Simulator results for the student you specify in the text entry. The "Run" option allows the program to run.

As you can see, it requires the selection of a .py file that will be stored in the Rules folder contained in the "backend". For this file to be detected as a rules override, it must be called "rules.py".

## Environment:

### Element:
It is a subject that focuses on an area of ​​knowledge.

An element can have a set of dependencies on other elements. That is, you cannot learn element e without learning element $e^{'}$, if the latter depends on $e$.

### Activity:
It is an action that enables the development of the learning process of certain elements.

An activity is defined as follows:
  - set of elements involved in the activity.
  - amount of knowledge points provided for each of the elements.
  - estimated duration time.

### Learning Environment:
An environment is defined by:
- a student.
- a set of elements.
- a set of activities.
- a set of rules.
 
The main entity that characterizes a learning environment is a student, whose purpose is to learn a subset of elements of the initial set (objectives), according to the conditions defined for him in said environment.

### Category:
Specifies a student's level of learning in a given element.

The existing categories are:
- learned.
- learnable.
- not learned.
- forgotten.

The transition from one category to another is determined by compliance with the rules.

## Problem modeling:

Let $E$ be a learning environment and a student $S$. We have to:

The set of elements of E can be represented as a directed graph $G = (V, A)$, where:
  - $V$ is the set of elements of $E$.
  - $A = {< e_1, e_2 > \in V × V : e_2 ∈ D(e_1)}$, with $D$ being the set of dependencies of $e_1$.

$G$ is a directed acyclic graph (DAG).

Compliance with the defined rules is verified to determine the learning level of student S in each of the vertices of G.

Since $G$ is a DAG, the set of possible learning strategies to satisfy the objectives of $S$ are topological orderings of $G$. Then the element $e$ can be learned when the constraints of that rule are validated according to its dependencies.

An ordered sequence of objectives to be learned is considered a solution to the problem. Some solutions may be better than others and the value against which they are compared is the percentage of learning obtained by carrying them out.

For each objective of the solution, several paths are sought in which to learn. These paths are found following different metrics: look for dependencies whose available points to obtain are greater or that the number of elements to learn so that their category improves is smaller, given that these have a higher degree of probability of success. Random paths are also searched to increase graph exploration. All of these paths are simulated multiple times, returning their average learning percentage and the time needed to complete them.

