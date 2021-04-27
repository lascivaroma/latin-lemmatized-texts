# Latin Lemmatized Texts

## Citation

Cite this corpus using the following:

```tex
@software{thibault_clerice_2020_corpus_latin,
  author       = {Clérice, Thibault},
  title        = {Corpus Latin antiquité et antiquité tardive lemmatisé},
  month        = apr,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {0.1.0},
  doi          = {10.5281/zenodo.4337145},
  url          = {https://doi.org/10.5281/zenodo.4337145}
}
```

## Information about the source corpora

This corpus contains the whole set of Capitains compliant classical and late Latin texts avaialable out there. The latest version of the corpus is based on the following corpora:


| Name                                                                            | Version | Project you need to cite                       |  
| ------------------------------------------------------------------------------- | ------- | ---------------------------------------------- | 
| [PerseusDL/canonical-latinLit](https://github.com/PerseusDL/canonical-latinLit) | 0.0.843 | https://www.perseus.org                        |
| [OpenGreekAndLatin/csel-dev](https://github.com/OpenGreekAndLatin/csel-dev)     | 1.0.211 | https://www.perseus.org                        |
| [OpenGreekAndLatin/Latin](https://github.com/OpenGreekAndLatin/Latin)           | v1.10.0 | https://www.perseus.org                        |
| [lascivaroma/digiliblt](https://github.com/lascivaroma/digiliblt)         | 0.0.62  | https://digiliblt.uniupo.it                    |
| [lascivaroma/priapeia](https://github.com/lascivaroma/priapeia)                 | 1.1.18  | [Lasciva Roma](https://github.com/lascivaroma) |
| [lascivaroma/additional-texts](https://github.com/lascivaroma/additional-texts) | 1.0.192 | [Lasciva Roma](https://github.com/lascivaroma) |


The texts are distributed using the same licence as the original, annotation are CC-BY-SA 4.0. 

<!--START-NB-->
**Number of tokens**: 20,505,245 (17,205,071 without punctuation)
<!--END-NB-->

## Information about the model

They were tagged with Pie-Extended LASLA model using the [0.0.6](https://github.com/PonteIneptique/latin-lasla-models/releases/tag/0.0.6) LASLA + model (trained with aligned PROIEL Vulgate as well as Priapea and a Late Latin Corpus to be published soon).


*Note:* the model is currently being fine-tuned in the context of my PhD. I'll fill this part when it will be done.

- Enclitics duplicate the whole token (-que are not separated). They are identifiable through as their form starts and ends with `{` and `}`. Example : 

```xml
  <w lemma="breuis" msd="Case=Abl|Numb=Plur|Gend=Com|Deg=Pos" n="1.18" pos="ADJqua" rend="section">breuibusque</w>
  <w lemma="que" msd="MORPH=empty" n="1.18" pos="CON" rend="section">{breuibusque}</w>
```

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

Tokens use the standard TEI annotation elements `@pos`, `@msd` and `@lemma`:

```xml
<w lemma="gaudeo" msd="Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1" n="7" pos="VER" rend="line">gaudeo</w>
```

## Lexical information and tags

### POS

| Tag        | French                          | English                          | UD POS | Example                                          |
|------------|---------------------------------|----------------------------------|--------|--------------------------------------------------|
| ADJadv.mul | Numéral Adverbial Multiplicatif | Multiplicative numeral adverbial | ADV    | quadragies                                       |
| ADJadv.ord | Numéral Adverbial Ordinal       | Ordinal numeral adverb           | ADV    | secundo                                          |
| ADJcar     | Numéral Cardinal                | Cardinal                         | NUM    | decem, ducenti, duo                              |
| ADJdis     | Numéral Distributif             | Distributive numeral             | ADJ    | tricenus, trinus, uicenus, undenus               |
| ADJmul     | Numéral Multiplicatif           | Multiplicative numeral           | ADJ    | septemplex, simplex, triplex                     |
| ADJord     | Numéral Ordinal                 | Ordinal numeral                  | ADJ    | octogesimus, primus, prior                       |
| ADJqua     | Adjectif qualificatif           | Adjective                        | ADJ    |                                                  |
| ADV        | Adverbe                         | Adverb                           | ADV    |                                                  |
| ADVint     | Adverbe interrogatif            | Interogative Adverb              | ADV    | an, anne, cuicuimodi2                            |
| ADVint.neg | Adverbe interrogatif négatif    | Negative Interrogative Adverb    | ADV    | necne, nonne, quidni                             |
| ADVneg     | Adverbe négatif                 | Negative Adverb                  | ADV    | haud, ne3, nec1                                  |
| ADVrel     | Adverbe relatif                 | Relative Adverb                  | ADV    | proquam, prout                                   |
| CONcoo     | Conjonction de coordination     | Coordinating conjunction         | CCONJ  |                                                  |
| CONsub     | Conjonction de subordination    | Subordinating conjunction        | SCONJ  |                                                  |
| INJ        | Interjection                    | Interjection                     | INTJ   |                                                  |
| NOMcom     | Nom commun                      | Noun                             | NOUN   |                                                  |
| NOMpro     | Nom propre                      | Proper Noun                      | PROPN  |                                                  |
| OUT        | Non-Géré                        | Out                              | X      |                                                  |
| PRE        | Préposition                     | Preposition                      | ADP    |                                                  |
| PROdem     | Pronom démonstratif             | Demonstrative Pronoun            | PRON   | hic, idem, ille                                  |
| PROind     | Pronom indéfini                 | Indefinite Pronoun               | PRON   | aliquantus, aliquis, aliquot, alis, alius, alter |
| PROint     | Pronom interrogatif             | Interrogative Pronoun            | PRON   | cuias, cuius, ecquis                             |
| PROper     | Pronom personnel                | Personal Pronoun                 | PRON   | ego, nos, tu, uos                                |
| PROpos     | Pronom possessif                | Possessive Pronoun               | PRON   | mei, meus, noster                                |
| PROpos.ref | Pronom possessif réfléchi       | Relfexive Possessive Pronoun     | PRON   | Sui, suus                                        |
| PROref     | Pronom réfléchi                 | Reflexive Pronoun                | PRON   | sepse, sui                                       |
| PROrel     | Pronom relatif                  | Relative Pronoun                 | PRON   | cuius, qualis, qualiscumque                      |
| PUNC       | Ponctuation                     | Punctuation                      | PUNCT  |                                                  |
| VER        | Verbe                           | Verb                             | VERB   |                                                  |
| VERaux     | Verbe auxiliaire                | Auxiliary Verb                   | AUX    |                                                  |
| FOR        | Termes étrangers                | Foreign words                    | X      |                                                  |

## Statistics

<!---START-STATS--->
| POS        |   Tokens |
|------------|----------|
|            |      274 |
| ADJadv.mul |     7336 |
| ADJadv.ord |    20543 |
| ADJcar     |   158149 |
| ADJdis     |    13445 |
| ADJmul     |     3912 |
| ADJord     |    58668 |
| ADJqua     |  1256850 |
| ADV        |   969879 |
| ADVint     |    64136 |
| ADVint.neg |     3279 |
| ADVneg     |   271514 |
| ADVrel     |   178543 |
| CON        |   171893 |
| CONcoo     |  1248073 |
| CONsub     |   585788 |
| FOR        |    35381 |
| INJ        |    28799 |
| NOM        |       28 |
| NOMcom     |  4135950 |
| NOMpro     |   661178 |
| PRE        |  1163671 |
| PROdem     |   755853 |
| PROind     |   366737 |
| PROint     |    77899 |
| PROper     |   238727 |
| PROpos     |   132758 |
| PROpos.ref |    81081 |
| PROref     |    77243 |
| PROrel     |   499688 |
| PUNC       |  3300174 |
| UNK        |      734 |
| VER        |  3934784 |
| _          |     2278 |
<!---END-STATS--->