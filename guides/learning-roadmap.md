# Learning Roadmap

A sequenced path for scientists who want to build solid software engineering (SE) foundations.
Start at the level that matches where you are, and work your way down.

---

**Beginner**
1. [Introduction to Version Control](#1-introduction-to-version-control)
2. [Data Structures & Algorithms](#2-data-structures--algorithms)
3. [Object-Oriented Programming](#3-object-oriented-programming)
4. [Developer Habits & Craft](#4-developer-habits--craft)

**Intermediate**
1. [Software Development Foundations](#1-software-development-foundations)
2. [Code Readability & Maintainability](#2-code-readability--maintainability)
3. [Automated Testing](#3-automated-testing)
4. [Software Design](#4-software-design)
5. [Data Modelling](#5-data-modelling)
6. [Continuous Integration & Delivery](#6-continuous-integration--delivery)
7. [Working with Existing Codebases](#7-working-with-existing-codebases)

**Advanced**
1. [Test-Driven Development](#1-test-driven-development)
2. [Software Architecture](#2-software-architecture)
3. [Advanced Testing Topics](#3-advanced-testing-topics)
4. [Containerization with Docker](#4-containerization-with-docker)

**AI-Assisted Coding**
1. [Software Engineering at a Tipping Point](#1-software-engineering-at-a-tipping-point)
2. [AI Coding Walkthroughs](#2-ai-coding-walkthroughs)
3. [Why Fundamentals Matter More Than Ever](#3-why-fundamentals-matter-more-than-ever)

---

## Beginner

> We assume you are a scientist or engineer who writes code to solve optimization or simulation
> problems, but have not formally studied software engineering.

### 1. Introduction to Version Control
*The practice of tracking changes to your code so you can collaborate, experiment safely, and recover from mistakes*

- 🎓 *Introduction to Git and GitHub* — Google Career Certificates | [Coursera](https://www.coursera.org/learn/introduction-git-github)

> Start here — adopt version control as your lab notebook before anything else.

---

### 2. Data Structures & Algorithms
*The core building blocks every programmer needs to reason about how data is organized and how algorithms operate on it*

- 🌐 *W3Schools DSA Intro* — [quick visual reference](https://www.w3schools.com/dsa/dsa_intro.php) for common structures and algorithms
- 🌐 *GeeksForGeeks DSA Tutorial* — [worked problems](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/) to build intuition through practice
- 🎓 *Data Structures and Algorithms* — UC San Diego | [Coursera specialization](https://www.coursera.org/specializations/data-structures-algorithms) with graded assignments

> Work through these before moving to intermediate resources — understanding how arrays,
> trees, and graphs work makes every modularity and complexity discussion much more concrete.

---

### 3. Object-Oriented Programming
*The paradigm behind most modern software frameworks — classes, objects, and the principles that make code modular and reusable*

- 🌐 *Introduction to OOP* — GeeksForGeeks | [conceptual intro](https://www.geeksforgeeks.org/dsa/introduction-of-object-oriented-programming/) covering classes, inheritance, encapsulation, and polymorphism
- 🎓 *Java Programming Fundamentals and OOP Concepts* — Packt | [Coursera](https://www.coursera.org/learn/packt-java-programming-fundamentals-and-object-oriented-concepts-ebdwt) — examples are in Java, but the OOP concepts transfer directly to Python

> Read this after DS&A — OOP gives you the vocabulary for how modules, interfaces, and
> dependency injection are structured.

---

### 4. Developer Habits & Craft
*How effective practitioners think about their code, tools, and long-term practices as working software developers*

- 📖 *The Pragmatic Programmer* — David Thomas & Andrew Hunt

> Read this after finishing your first real project — the advice will make immediate
> sense once you have felt the pain it describes.

---

## Intermediate

### 1. Software Development Foundations
*What software engineering is as a discipline, how the development process works, and the principles that separate good code from research scripts*

- 📖 *Head First Software Development* — Andrew Stellman & Jennifer Greene
- 📖 *Clean Agile: Back to Basics* — Robert C. Martin
- 📖 *Modern Software Engineering* — David Farley

> Read these once you have Git fluency and basic DS&A — together they cover the process,
> the mindset, and the theoretical grounding behind every practice that follows.

---

### 2. Code Readability & Maintainability
*How to write code that humans can read, understand, and change — naming, functions, and structure at the line and module level*

- 📖 *Clean Code* — Robert C. Martin

> Read this once you have working code and want to make it readable and maintainable
> for your future self and collaborators.

---

### 3. Automated Testing
*How to write tests that give you genuine confidence in your code — not just tests that pass, but tests that are meaningful and maintainable*

- 📖 *Unit Testing: Principles, Practices and Patterns* — Vladimir Khorikov
- 📖 *Effective Software Testing: A developer's guide* — Mauricio Aniche

> Read this when you start writing tests and want to understand what separates a useful
> test from a fragile one.

---

### 4. Software Design
*How to manage complexity through deep modules, simple interfaces, and deliberate information hiding — a rigorous framework for thinking about system design*

- 📖 *A Philosophy of Software Design* — John Ousterhout
- 🌐 *A Philosophy of Software Design* | John Ousterhout | Talks at Google [Video](https://www.youtube.com/watch?v=bmSAYlu0NcY)
- 🌐 *Refactoring Guru: Design Patterns* — [refactoring.guru/design-patterns](https://refactoring.guru/design-patterns): a visual catalog of classic design patterns with examples and use cases

> Read this after building several projects — it rewards readers who have already felt
> the pain of systems that became too complex to change.

---

### 5. Data Modelling
*How to represent real-world information as structured data — designing tables, relationships, and schemas that are accurate, consistent, and easy to query*

- 📖 *Database Design for Mere Mortals* — Michael J. Hernandez

> Read this when your research code starts managing non-trivial data — instances, solutions,
> parameters — and you need a principled way to structure and store it.

---

### 6. Continuous Integration & Delivery
*The practice of automatically building, testing, and deploying your code on every change — so problems surface immediately and releases stay reliable*

- 🌐 *GitHub Actions* — [official documentation](https://docs.github.com/en/actions): the most practical starting point if your code lives on GitHub
- 🎓 *Continuous Integration and Continuous Delivery (CI/CD)* — [Coursera](https://www.coursera.org/learn/continuous-integration-and-continuous-delivery-ci-cd): structured course covering pipelines, automation, and delivery workflows
- 📖 *Continuous Delivery* — Jez Humble & Dave Farley: the definitive text on building reliable, automated delivery pipelines

> Read this after you have a working test suite — CI is what runs those tests automatically
> on every change, turning manual discipline into a system that enforces itself.

---

### 7. Working with Existing Codebases
*How to safely understand, navigate, and improve code you did not write — without breaking what already works*

- 📖 *Working Effectively with Legacy Code* (Robert C. Martin Series) — Michael Feathers

> Read this when you inherit a codebase with no tests or unclear structure — Feathers gives
> concrete techniques for adding tests and making changes safely, one seam at a time.

---

## Advanced

### 1. Test-Driven Development
*A discipline where you write the test before the code — using failing tests to drive design decisions and keep the codebase honest*

- 📖 *Test-Driven Development by Example* — Kent Beck

> Read this after you are comfortable with automated testing — TDD is not just a testing
> technique but a design practice that changes how you think about building software.

---

### 2. Software Architecture
*How to structure large systems into layers, components, and boundaries so that business logic stays independent of frameworks, databases, and delivery mechanisms*

- 📖 *Clean Architecture* — Robert C. Martin

> Read this after Software Design — it scales the same principles (separation of
> concerns, information hiding) up to the level of entire systems.

---

### 3. Advanced Testing Topics
*Techniques for measuring and improving the quality of your test suite — beyond writing tests to understanding whether they actually work*

#### Code Coverage
*A metric that tracks which lines of code your tests execute — useful as a signal, dangerous as a goal*

- 🌐 *Code Coverage Best Practices* — Google Testing Blog | [testing.googleblog.com](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html): how Google thinks about coverage — what it tells you, what it doesn't, and how to avoid the common trap of optimizing for the number

#### Mutation Testing
*Deliberately introducing small bugs into your code to check whether your tests catch them — a stronger signal than coverage alone*

- 🌐 *Mutation Testing* — GeeksForGeeks | [conceptual introduction](https://www.geeksforgeeks.org/software-engineering/software-testing-mutation-testing/) to the technique and its operators
- 🌐 *PIT Mutation Testing* — [pitest.org](https://pitest.org/): the leading mutation testing tool for JVM languages, with concepts that apply across ecosystems

> Read the coverage article first — it reframes what "enough testing" means. Then read
> mutation testing to learn a concrete method for answering that question.

---

### 4. Containerization with Docker
*Packaging your code and all its dependencies into a portable, isolated environment that runs identically on any machine*

- 📺 *Docker in 100 Seconds* — Fireship | [YouTube](https://www.youtube.com/watch?v=b0HMimUb4f0): a fast conceptual overview of what Docker is and why it matters
- 🌐 *Docker 101 Tutorial* — Docker Inc. | [docker.com](https://www.docker.com/101-tutorial/): official hands-on introduction to building and running containers

> Read this once you have a working project and want to guarantee that anyone — a collaborator,
> a reviewer, or your future self on a new machine — can run it without environment headaches.

---

## AI-Assisted Coding

> The skills in this roadmap become more valuable, not less, as AI coding assistants improve.
> AI amplifies the engineering practices already present — understand the foundations first.

### 1. Software Engineering in the AI era
*A high-level perspective on how AI coding assistants are shifting the nature of software work and what that means for practitioners*

- 📺 *Software Engineering at a Tipping Point* — Google Engineering | [YouTube](https://www.youtube.com/watch?v=2n41YjR5QfU)

> Watch this first — it frames the conversation about AI and SE before diving into practical workflows.

---

### 2. AI-Assisted Strategies
*Concrete demonstrations of how experienced practitioners use AI coding assistants in their day-to-day workflow*

- 📺 *Full Walkthrough: Workflow for AI Coding* — Matt Pocock | [YouTube](https://www.youtube.com/watch?v=-QFHIoCo-Ko)
- 🎓 *CS106S: The Modern Software Developer* — Stanford University | [themodernsoftware.dev](https://themodernsoftware.dev/)
- 🌐 *The New SDLC With Vibe Coding* - Google | [Kaggle](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding)

> Watch this to see how SE habits (modularity, tests, clear interfaces) make AI assistance more effective in practice.

---

### 3. Why Fundamentals Matter More Than Ever
*The case that software engineering foundations become more — not less — important as AI tools take over routine code generation*

- 📺 *Software Fundamentals Matter More Than Ever* — [YouTube](https://www.youtube.com/watch?v=v4F1gFy-hqg)

> Watch this after working through the Intermediate section — the argument lands hardest once you have experienced the fundamentals firsthand.
