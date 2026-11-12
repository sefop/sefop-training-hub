# DecisionOps in practice

**A practical e-book to implement DecisionOps**

by Francisco Zenteno Smith

This book serves two audiences:

1. **Operations research scientists** who want to ship decision-support software with professional standards.
2. **Engineering managers** who lead the teams building them.

> [!NOTE]
> This book is under construction. Nothing is definitive yet.

---

## Book contents

| # | Chapter | Questions it answers |
|:---:|---|---|
| 01 | [Introduction](book/01-introduction/README.md) | • What is decision-support software, and how does it differ from a one-off analysis?<br>• Why does decision-support software so often become hard to maintain?<br>• What is DecisionOps, and how does it relate to DevOps and MLOps? |
| 02 | [Lifecycle](book/02-lifecycle/README.md) | • Why is software engineering different from other engineering?<br>• How does a team learn and adapt quickly, and what do the Three Ways of DevOps add?<br>• What changes in each lifecycle phase when the software produces decisions? |
| 03 | [Design](book/03-design/README.md) | • Why invest in design when the software already works?<br>• Which principles, contracts and patterns keep a decision-support system easy to change?<br>• How do I arrange the optimization module within the system's architecture? |
| 04 | [Testing](book/04-testing/README.md) | • What should I test in a decision-support system?<br>• How do I test a model when I don't know its optimal answer?<br>• Which tests still work when the solver is a heuristic? |
| 05 | [Deployment](book/05-deployment/README.md) | • How do I package and deploy a model with its solver?<br>• What should happen when a run cannot deliver an acceptable plan?<br>• How do I assess a new version on the same instances, release it safely, and recover? |
| 06 | [Operating and evaluating](book/06-operating/README.md) | • What should I measure to know whether runs are healthy?<br>• How do I know whether the decisions are actually used and useful?<br>• When should we keep investing in a system, change it, or retire it? |
| 07 | [Adopting DecisionOps](book/07-adopting/README.md) | • How do I start a new decision-support system with these practices from day one?<br>• How do I make an inherited system safer to change, and bring the team along?<br>• Which roles, time and training does my team need from its leaders? |

---

## Appendix

- [Learning Roadmap](book/appendix/learning-roadmap.md): a suggested order to learn software engineering for building decision-support software.
- [Practice Repositories](book/appendix/practice-repositories.md): language-specific exercises.
- [Glossary](book/appendix/glossary.md): every software engineering term used in the book, defined once.


## For Questions

Go here <https://github.com/orgs/sefop/discussions>.

## How to cite

Zenteno Smith, F. (2026). _DecisionOps in practice: A practical e-book to implement DecisionOps_.
E-book, under construction. <https://github.com/sefop/sefop-training-hub>

```bibtex
@misc{zentenosmith2026decisionops,
  author       = {Zenteno Smith, Francisco},
  title        = {{DecisionOps} in practice: A practical e-book to implement {DecisionOps}},
  year         = {2026},
  howpublished = {\url{https://github.com/sefop/sefop-training-hub}},
  note         = {E-book, under construction}
}
```

## License

The text and figures are copyright 2026 Francisco Zenteno Smith and licensed under
[CC BY 4.0](LICENSE): you may share and adapt them, even commercially, as long as you credit the
author. The code (`book/05-deployment/assets/source/`) is licensed under the
[MIT License](LICENSE-CODE).
