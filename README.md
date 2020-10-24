# Latin Lemmatized Texts

## Citation

Cite this corpus using the following:


```tex
@software{thibault_clerice_2020_corpus_latin,
  author       = {Clérice, Thibault},
  title        = {Corpus Latin antiquité et antiquité tardive lemmatisé},
  month        = oct,
  year         = 2020,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.3883589},
  url          = {https://github.com/lascivaroma/latin-lemmatized-texts}
}
```

## Information about the source corpora

This corpus contains the whole set of Capitains compliant classical and late Latin texts avaialable out there. The latest version of the corpus is based on the following corpora:

| Name                                                                            | Version | Project you need to cite                       |  
| ------------------------------------------------------------------------------- | ------- | ---------------------------------------------- | 
| [PerseusDL/canonical-latinLit](https://github.com/PerseusDL/canonical-latinLit) | 0.0.557 | https://www.perseus.org                        |
| [OpenGreekAndLatin/csel-dev](https://github.com/OpenGreekAndLatin/csel-dev)     | 1.0.67  | https://www.perseus.org                        |
| [OpenGreekAndLatin/Latin](https://github.com/OpenGreekAndLatin/Latin)           | v1.10.0 | https://www.perseus.org                        |
| [ponteineptique/digiliblt](https://github.com/ponteineptique/digiliblt)         | 0.0.32  | https://digiliblt.uniupo.it                    |
| [lascivaroma/priapeia](https://github.com/lascivaroma/priapeia)                 | 1.1.18  | [Lasciva Roma](https://github.com/lascivaroma) |
| [lascivaroma/additional-texts](https://github.com/lascivaroma/additional-texts) | 1.0.115 | [Lasciva Roma](https://github.com/lascivaroma) |


The texts are distributed using the same licence as the original, annotation are CC-BY-SA 4.0. 

## Information about the model

They were tagged with Pie-Extended LASLA model using the [0.0.4](https://github.com/PonteIneptique/latin-lasla-models/releases/tag/0.0.4) version's Vulgate Model.


*Note:* the model is currently being fine-tuned in the context of my PhD. I'll fill this part when it will be done.

- Enclitics duplicates the whole token (-que are not separated). They are identifiable through as their form starts and ends with `{` and `}`.
- Roman numbers are lemmatized as Arabic numbers.
- The model is highly susceptible of wrong annotation for wrong tokens such as `7AP`.
- Tokens ending with `?` are known as needing disambiguation but disambiguation was not possible (there seems to have been an issue with some automatic ones in this version of the corpus).

## Information about the schema

XML Files are TEI compliant (normally) and the text in separated in passages, their type being provided at the `ab` level.

```xml
    <text n="urn:cts:latinLit:phi0119.phi009.perseus-lat2">
        <body>
          <ab n="urn:cts:latinLit:phi0119.phi009.perseus-lat2:1" type="line">
```

Tokens use the standard TEI annotation elements:

```xml
<w lemma="gaudeo" msd="Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1" n="7" pos="VER" rend="line">gaudeo</w>
```

