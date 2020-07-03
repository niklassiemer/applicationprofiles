# ApplicationProfiles

This repository contains all CoScInE application profiles.

#### Proposed Structure:
- `ontologies` Folder:  contains subfolders with full schema definitions (properties + "word lists") of external definitions, no shapes
  - e.g. `index.ttl` for the definition of "external" properties like dcterms:title of Dublin Core metadata schema
- `profiles` Folder: Contains application profiles
  - e.g. `radar/index.ttl` with the application profile.
- `terms` Folder:  contains subfolders with full schema definitions (properties + "word lists"), no shapes
  - e.g. `index.ttl` for the definition of "internal" properties like current coscineode:simulation and its possible values
  - later for definition of fields we may need when converting current forms.
- `vocabularies` Folder: Contains "word lists" with a subfolder structure, no shapes
  - e.g. `dc/dcmitype/index.ttl` for the dublin core types. Try to stick to the usual naming conventions for the prefixes in Turtle.
  - e.g. `dfg/dfgs/index.ttl` for  DFG Fachsystematik.


Stick to lower case letters for all folders.

Use `purl.org/coscine/` as prefix.

File structure:
- Files containing Turtle syntax should have `.ttl` ending.
- Make sure `.ttl` are valid. E.g. define prefixes like rwth (unlike [here](https://git.rwth-aachen.de/coscine/applicationprofiles/blob/b1acec31d467692063b2e59e24cdec133a85c4ab/Vocabularies/PublishMetadata/PublishMetadata.rdf))
- Make sure every file has a self descriptive "header" like 
```ttl
<http://purl.org/coscine/terms/> # redirects to /terms/index.ttl in this repo
    dcterms:license <https://spdx.org/licenses/MIT> ;
    dcterms:publisher <https://itc.rwth-aachen.de> ;
    dcterms:rights "Copyright © 2020 IT Center, RWTH Aachen University" ;
    dcterms:title "Coscine Technical Metadata"@en .
```
including a (`dcterms:license` and `dcterms:publisher`) or `dcterms:rights` statement. The example above has both for illustration purposes. If other information like creator are available include them or leave them in. Refere to https://spdx.org/licenses/ for license URLs.

Redirections:
- `https://purl.org/coscine/ontologies/` will redirect to the ontolgies folder and subfolders
- `https://purl.org/coscine/ap/` will redirect to the profiles folder and subfolders
- `https://purl.org/coscine/terms/` will redirect to the terms folder and subfolders
- `https://purl.org/coscine/voc/` will redirect to the vocabularies folder and subfolders

