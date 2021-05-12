import shutil
from glob import iglob
import os

from gen_experimental_schemes import schemes_to_write as experimental_schemes
from gen_digital_schemes import schemes_to_write as digital_schemes


for n, class_ in enumerate(list(experimental_schemes.values()) + list(digital_schemes.values())):
    if n == 0:
        MasterScheme = type("TransientClass" + str(n), tuple([class_]), {})
    else:
        MasterScheme = type("TransientClass"+str(n), tuple([MasterScheme, class_]), {})


def remove_duplications(term_list):
    sfb_terms_ids = [item.split()[0] for item in term_list]

    unique_term_ids = []
    duplicated_idx = {}
    failure = False
    msg = ""

    for n, ID in enumerate(sfb_terms_ids):
        if ID not in unique_term_ids:
            unique_term_ids.append(ID)
            if n+1 < len(sfb_terms_ids):
                duplication_idxs = []
                for n2, ID2 in enumerate(sfb_terms_ids[n+1:]):
                    if ID == ID2:
                        duplication_idxs.append(n+n2+1)
                if len(duplication_idxs) > 0:
                    duplicated_idx[ID] = [n] + duplication_idxs

    for key, value in duplicated_idx.items():
        different_output = [term_list[value[0]]]
        for indx in value[1:]:
            if term_list[value[0]] != term_list[indx] and term_list[indx] not in different_output:
                different_output.append(term_list[indx])
        if len(different_output) > 1:
            failure = True
            msg += f'Not matching entries for {key}! \n'
            for output in different_output:
                msg += "-----  \n "
                msg += output + "\n "

    if failure:
        raise ValueError("Not matching Entries found: \n" + msg)

    return list(set(term_list))


MasterScheme = MasterScheme()

sfb_terms = [field.ttl_term_str for field in MasterScheme if field.ttl_term_str != ""]
sfb_terms = remove_duplications(sfb_terms)
sfb_terms.sort()

preamble = '''@base  <http://purl.org/coscine/terms/sfb1394/> .
@prefix sfb1394: <http://purl.org/coscine/terms/sfb1394#> .

@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

<http://purl.org/coscine/terms/sfb1394/>
dcterms:publisher <http://www.itc.rwth-aachen.de/> ;
dcterms:license <http://spdx.org/licenses/CC-BY-4.0> ;
dcterms:rights "Copyright © 2020 RWTH Aachen University" ;
dcterms:title "SFB1394 Metadata"@en 
.
\n'''

with open("sfb1394_terms.ttl", 'w', encoding='utf8') as f:
    f.write(preamble)
    for term in sfb_terms:
        f.write(term)


vocab_prefix = """@base  <http://purl.org/coscine/vocabularies/sfb1394/> .

@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

"""
with open('sfb1394_vocab.ttl', 'w', encoding='utf8') as result_file:
    result_file.write(vocab_prefix)
    for vocab_file in iglob("*_vocab.ttl"):
        with open(vocab_file) as f:
            result_file.write(f.read())


root_dir = os.path.normpath(os.path.join(os.getcwd(), '../../'))
vocab_dir = os.path.join(root_dir, 'vocabularies/sfb1394')
term_dir = os.path.join(root_dir, 'terms/sfb1394')
profiles_dir = os.path.join(root_dir, 'profiles/sfb1394')

try:
    os.mkdir(vocab_dir)
except FileExistsError:
    pass

shutil.copy('sfb1394_vocab.ttl', os.path.join(vocab_dir, 'index.ttl'))

shutil.copy('sfb1394_terms.ttl', os.path.join(term_dir, 'index.ttl'))

for scheme_name in list(experimental_schemes.keys()) + list(digital_schemes.keys()):
    scheme_dir = os.path.join(profiles_dir, scheme_name)
    try:
        os.mkdir(scheme_dir)
    except FileExistsError:
        pass
    shutil.copy(scheme_name+'.ttl', os.path.join(scheme_dir, 'index.ttl'))
