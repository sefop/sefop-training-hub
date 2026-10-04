# Learning Roadmap

A sequenced path for scientists who want to build solid software engineering (SE) foundations. Start
at the level that matches where you are, and work your way down.

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
6. [DevOps](#6-devops)
7. [Working with Existing Codebases](#7-working-with-existing-codebases)

**Advanced**

1. [Engineering Over Time](#1-engineering-over-time)
2. [Software Architecture](#2-software-architecture)
3. [Advanced Testing Topics](#3-advanced-testing-topics)
4. [Containerization with Docker](#4-containerization-with-docker)

**AI-Assisted Coding**

1. [Software Engineering in the AI era](#1-software-engineering-in-the-ai-era)
2. [AI-Assisted Strategies](#2-ai-assisted-strategies)
3. [Why Fundamentals Matter More Than Ever](#3-why-fundamentals-matter-more-than-ever)

---

## Beginner

> We assume you are a scientist or engineer who writes code to solve optimization or simulation
> problems, but have not formally studied software engineering.

### 1. Introduction to Version Control

_The practice of tracking changes to your code so you can collaborate, experiment safely, and
recover from mistakes_

- 🎓 _Introduction to Git and GitHub_ — Google Career Certificates |
  [Coursera](https://www.coursera.org/learn/introduction-git-github)

> Start here — adopt version control as your lab notebook before anything else.

---

### 2. Data Structures & Algorithms

_The core building blocks every programmer needs to reason about how data is organized and how
algorithms operate on it_

- 🌐 _W3Schools DSA Intro_ — [quick visual reference](https://www.w3schools.com/dsa/dsa_intro.php)
  for common structures and algorithms
- 🌐 _GeeksForGeeks DSA Tutorial_ —
  [worked problems](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)
  to build intuition through practice
- 🎓 _Data Structures and Algorithms_ — UC San Diego |
  [Coursera specialization](https://www.coursera.org/specializations/data-structures-algorithms)
  with graded assignments

> Work through these before moving to intermediate resources — understanding how arrays, trees, and
> graphs work makes every modularity and complexity discussion much more concrete.

---

### 3. Object-Oriented Programming

_The paradigm behind most modern software frameworks — classes, objects, and the principles that
make code modular and reusable_

- 🌐 _Introduction to OOP_ — GeeksForGeeks |
  [conceptual intro](https://www.geeksforgeeks.org/dsa/introduction-of-object-oriented-programming/)
  covering classes, inheritance, encapsulation, and polymorphism
- 🎓 _Java Programming Fundamentals and OOP Concepts_ — Packt |
  [Coursera](https://www.coursera.org/learn/packt-java-programming-fundamentals-and-object-oriented-concepts-ebdwt)
  — examples are in Java, but the OOP concepts transfer directly to Python

> Read this after DS&A — OOP gives you the vocabulary for how modules, interfaces, and dependency
> injection are structured.

---

### 4. Developer Habits & Craft

_How effective practitioners think about their code, tools, and long-term practices as working
software developers_

- 📖 _The Pragmatic Programmer_ — David Thomas & Andrew Hunt

> Read this after finishing your first real project — the advice will make immediate sense once you
> have felt the pain it describes.

---

## Intermediate

### 1. Software Development Foundations

_What software engineering is as a discipline, how the development process works, and the principles
that separate good code from research scripts_

- 📖 _Head First Software Development_ — Andrew Stellman & Jennifer Greene
- 📖 _Clean Agile: Back to Basics_ — Robert C. Martin
- 📖 _Modern Software Engineering_ — David Farley

> Read these once you have Git fluency and basic DS&A — together they cover the process, the
> mindset, and the theoretical grounding behind every practice that follows.

---

### 2. Code Readability & Maintainability

_How to write code that humans can read, understand, and change — naming, functions, and structure
at the line and module level_

- 📖 _Clean Code_ — Robert C. Martin

> Read this once you have working code and want to make it readable and maintainable for your future
> self and collaborators.

---

### 3. Automated Testing

_How to write tests that give you genuine confidence in your code — not just tests that pass, but
tests that are meaningful and maintainable_

- 📖 _Unit Testing: Principles, Practices and Patterns_ — Vladimir Khorikov
- 📖 _Effective Software Testing: A developer's guide_ — Mauricio Aniche

> Read this when you start writing tests and want to understand what separates a useful test from a
> fragile one.

---

### 4. Software Design

_How to manage complexity through deep modules, simple interfaces, and deliberate information hiding
— a rigorous framework for thinking about system design_

- 📖 _A Philosophy of Software Design_ — John Ousterhout
- 🌐 _A Philosophy of Software Design_ | John Ousterhout | Talks at Google
  [Video](https://www.youtube.com/watch?v=bmSAYlu0NcY)
- 🌐 _Refactoring Guru: Design Patterns_ —
  [refactoring.guru/design-patterns](https://refactoring.guru/design-patterns): a visual catalog of
  classic design patterns with examples and use cases

> Read this after building several projects — it rewards readers who have already felt the pain of
> systems that became too complex to change.

---

### 5. Data Modelling

_How to represent real-world information as structured data — designing tables, relationships, and
schemas that are accurate, consistent, and easy to query_

- 📖 _Database Design for Mere Mortals_ — Michael J. Hernandez

> Read this when your research code starts managing non-trivial data — instances, solutions,
> parameters — and you need a principled way to structure and store it.

---

### 6. DevOps

_The practice of automatically building, testing, and deploying your code on every change — so
problems surface immediately and releases stay reliable_

- 🌐 _GitHub Actions_ — [official documentation](https://docs.github.com/en/actions): the most
  practical starting point if your code lives on GitHub
- 🎓 _Continuous Integration and Continuous Delivery (CI/CD)_ —
  [Coursera](https://www.coursera.org/learn/continuous-integration-and-continuous-delivery-ci-cd):
  structured course covering pipelines, automation, and delivery workflows
- 📖 _Continuous Delivery_ — Jez Humble & Dave Farley: the definitive text on building reliable,
  automated delivery pipelines
- 📖 _The Phoenix Project_ — Gene Kim, Kevin Behr & George Spafford: a novel that dramatizes DevOps
  principles through the story of an IT organization in crisis

> Read this after you have a working test suite — CI is what runs those tests automatically on every
> change, turning manual discipline into a system that enforces itself.

---

### 7. Working with Existing Codebases

_How to safely understand, navigate, and improve code you did not write — without breaking what
already works_

- 📖 _Working Effectively with Legacy Code_ (Robert C. Martin Series) — Michael Feathers

> Read this when you inherit a codebase with no tests or unclear structure — Feathers gives concrete
> techniques for adding tests and making changes safely, one seam at a time.

---

## Advanced

### 1. Engineering Over Time

_What separates writing code from sustaining it — how software survives years of change, growing
teams, and dependencies nobody controls_

- 📖 _Software Engineering at Google_ — Titus Winters, Tom Manshreck & Hyrum Wright |
  [free online](https://abseil.io/resources/swe-book)

> Read this once you have shipped something that outlived its first deadline. Its thesis — that
> software engineering is programming integrated over time — is the argument this book makes about
> decision-support systems, told at the scale of thousands of engineers.

---

### 2. Software Architecture

_How to structure large systems into layers, components, and boundaries so that business logic stays
independent of frameworks, databases, and delivery mechanisms_

- 📖 _Clean Architecture_ — Robert C. Martin

> Read this after Software Design — it scales the same principles (separation of concerns,
> information hiding) up to the level of entire systems.

---

### 3. Advanced Testing Topics

_Disciplines and measurements that raise the quality of a test suite — from letting tests drive the
design to finding out whether they actually work_

#### Test-Driven Development

_Writing the test before the code, in short cycles — using failing tests to drive design decisions
and keep the codebase honest_

- 📖 _Test-Driven Development by Example_ — Kent Beck

#### Code Coverage

_A metric that tracks which lines of code your tests execute — useful as a signal, dangerous as a
goal_

- 🌐 _Code Coverage Best Practices_ — Google Testing Blog |
  [testing.googleblog.com](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html):
  how Google thinks about coverage — what it tells you, what it doesn't, and how to avoid the common
  trap of optimizing for the number

#### Mutation Testing

_Deliberately introducing small bugs into your code to check whether your tests catch them — a
stronger signal than coverage alone_

- 🌐 _Mutation Testing_ — GeeksForGeeks |
  [conceptual introduction](https://www.geeksforgeeks.org/software-engineering/software-testing-mutation-testing/)
  to the technique and its operators
- 🌐 _PIT Mutation Testing_ — [pitest.org](https://pitest.org/): the leading mutation testing tool
  for JVM languages, with concepts that apply across ecosystems

> Start with TDD once you are comfortable writing automated tests — it is a design practice as much
> as a testing one, and it changes how you think about building software. Then read the coverage
> article, which reframes what "enough testing" means, and finish with mutation testing for a
> concrete method of answering that question.

---

### 4. Containerization with Docker

_Packaging your code and all its dependencies into a portable, isolated environment that runs
identically on any machine_

- 📺 _Docker in 100 Seconds_ — Fireship | [YouTube](https://www.youtube.com/watch?v=b0HMimUb4f0): a
  fast conceptual overview of what Docker is and why it matters
- 🌐 _Docker 101 Tutorial_ — Docker Inc. | [docker.com](https://www.docker.com/101-tutorial/):
  official hands-on introduction to building and running containers

> Read this once you have a working project and want to guarantee that anyone — a collaborator, a
> reviewer, or your future self on a new machine — can run it without environment headaches.

---

## AI-Assisted Coding

> The skills in this roadmap become more valuable, not less, as AI coding assistants improve. AI
> amplifies the engineering practices already present — understand the foundations first.

### 1. Software Engineering in the AI era

_A high-level perspective on how AI coding assistants are shifting the nature of software work and
what that means for practitioners_

- 📺 _Software Engineering at a Tipping Point_ — Google Engineering |
  [YouTube](https://www.youtube.com/watch?v=2n41YjR5QfU)

> Watch this first — it frames the conversation about AI and SE before diving into practical
> workflows.

---

### 2. AI-Assisted Strategies

_Concrete demonstrations of how experienced practitioners use AI coding assistants in their
day-to-day workflow_

- 📺 _Full Walkthrough: Workflow for AI Coding_ — Matt Pocock |
  [YouTube](https://www.youtube.com/watch?v=-QFHIoCo-Ko)
- 🎓 _CS106S: The Modern Software Developer_ — Stanford University |
  [themodernsoftware.dev](https://themodernsoftware.dev/)
- 🌐 _The New SDLC With Vibe Coding_ - Google |
  [Kaggle](https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding)
- 📺 _Don't Ship Skills Without Evals_ — Philipp Schmid (Google DeepMind) |
  [YouTube](https://www.youtube.com/watch?v=0vphxNt4wyk)

> Watch this to see how SE habits (modularity, tests, clear interfaces) make AI assistance more
> effective in practice.

---

### 3. Why Fundamentals Matter More Than Ever

_The case that software engineering foundations become more — not less — important as AI tools take
over routine code generation_

- 📺 _Software Fundamentals Matter More Than Ever_ —
  [YouTube](https://www.youtube.com/watch?v=v4F1gFy-hqg)

> Watch this after working through the Intermediate section — the argument lands hardest once you
> have experienced the fundamentals firsthand.
