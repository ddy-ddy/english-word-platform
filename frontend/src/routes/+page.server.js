/*
 * @Author: ddy 58058861+ddy-ddy@users.noreply.github.com
 * @Date: 2023-03-07 22:23:47
 * @LastEditTime: 2023-03-28 09:36:23
 * @Github: https://github.com/ddy-ddy
 * @Website: https://ddy-ddy.com
 */
import { error } from '@sveltejs/kit';

const info = {
    'id': '0',
    'nodeType': 'query',
    'name': 'implicit',
    'status': 'R',
    'relation': '',
    'pos': '',
    'examples': '',
    'definition': '',
    'children': [
        {
            'id': 'implicit.s.02',
            'name': 'implicit, unquestioning',
            'status': 'R',
            'relation': 'InSynset',
            'pos': 's',
            'examples': "['implicit trust']",
            'definition': 'being without doubt or reserve',
            'label': '(s)being without doubt or reserve',
            'children': [
                {
                    'id': 'absolute.a.01',
                    'name': 'absolute',
                    'status': 'G',
                    'relation': 'SimilarTo',
                    'pos': 'a',
                    'examples': "['absolute loyalty', 'absolute silence', 'absolute truth', 'absolute alcohol']",
                    'definition': 'perfect or complete or pure',
                    'label': '(a)perfect or complete or pure',
                    'children': [
                        {
                            'id': 'direct.s.10',
                            'name': 'direct',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 's',
                            'examples': "['the direct opposite']",
                            'definition': 'lacking compromising or mitigating elements; exact',
                            'label': '(s)lacking compromising or mitigating elements; exact',
                            'children': []
                        },
                        {
                            'id': 'implicit.s.023',
                            'name': 'unquestioning, implicit',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 's',
                            'examples': "['implicit trust']",
                            'definition': 'being without doubt or reserve',
                            'label': '(s)being without doubt or reserve',
                            'children': []
                        },
                        {
                            'id': 'infinite.s.04',
                            'name': 'infinite',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 's',
                            'examples': '["God\'s infinite wisdom"]',
                            'definition': 'total and all-embracing',
                            'label': '(s)total and all-embracing',
                            'children': []
                        },
                        {
                            'id': 'living.s.03',
                            'name': 'living',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 's',
                            'examples': "['she is a living doll', 'scared the living daylights out of them', 'beat the living hell out of him']",
                            'definition': '(informal) absolute',
                            'label': '(s)(informal) absolute',
                            'children': []
                        },
                        {
                            'id': 'relative.a.01',
                            'name': 'comparative, relative',
                            'status': 'G',
                            'relation': 'Antonym',
                            'pos': 'a',
                            'examples': "['a relative stranger']",
                            'definition': 'estimated by comparison; not absolute or complete',
                            'label': '(a)estimated by comparison; not absolute or complete',
                            'children': []
                        }
                    ]
                }
            ]
        },
        {
            'id': 'implicit.a.01',
            'name': 'implicit, inexplicit',
            'status': 'R',
            'relation': 'InSynset',
            'pos': 'a',
            'examples': "['an implicit agreement not to raise the subject', 'there was implicit criticism in his voice', 'anger was implicit in the argument', 'the oak is implicit in the acorn']",
            'definition': 'implied though not directly expressed; inherent in the nature of something',
            'label': '(a)implied though not directly expressed; inherent in the nature of something',
            'children': [
                {
                    'id': 'explicitness.n.01',
                    'name': 'explicitness',
                    'status': 'G',
                    'relation': 'Attribute',
                    'pos': 'n',
                    'examples': '[]',
                    'definition': 'clarity as a consequence of being explicit',
                    'label': '(n)clarity as a consequence of being explicit',
                    'children': [
                        {
                            'id': 'clarity.n.01',
                            'name': 'limpidity, clearness, pellucidity, lucidness, lucidity, clarity',
                            'status': 'G',
                            'relation': 'IsA',
                            'pos': 'n',
                            'examples': '[]',
                            'definition': 'free from obscurity and easy to understand; the comprehensibility of clear expression',
                            'label': '(n)free from obscurity and easy to understand; the comprehensibility of clear expression',
                            'children': []
                        },
                        {
                            'id': 'inexplicitness.n.01',
                            'name': 'inexplicitness',
                            'status': 'G',
                            'relation': 'Antonym',
                            'pos': 'n',
                            'examples': '[]',
                            'definition': 'unclearness by virtue of not being explicit',
                            'label': '(n)unclearness by virtue of not being explicit',
                            'children': []
                        },
                        {
                            'id': 'explicit.a.01',
                            'name': 'expressed, explicit',
                            'status': 'G',
                            'relation': 'Attribute',
                            'pos': 'a',
                            'examples': "['explicit instructions', 'she made her wishes explicit', 'explicit sexual scenes']",
                            'definition': 'precisely and clearly expressed or readily observable; leaving nothing to implication',
                            'label': '(a)precisely and clearly expressed or readily observable; leaving nothing to implication',
                            'children': []
                        },
                        {
                            'id': 'implicit.a.0113',
                            'name': 'inexplicit, implicit',
                            'status': 'G',
                            'relation': 'Attribute',
                            'pos': 'a',
                            'examples': "['an implicit agreement not to raise the subject', 'there was implicit criticism in his voice', 'anger was implicit in the argument', 'the oak is implicit in the acorn']",
                            'definition': 'implied though not directly expressed; inherent in the nature of something',
                            'label': '(a)implied though not directly expressed; inherent in the nature of something',
                            'children': []
                        }
                    ]
                },
                {
                    'id': 'implicit_in.s.01',
                    'name': 'underlying, inherent, implicit_in',
                    'status': 'G',
                    'relation': 'SimilarTo',
                    'pos': 's',
                    'examples': "['shortcomings inherent in our approach', 'an underlying meaning']",
                    'definition': 'in the nature of something though not readily apparent',
                    'label': '(s)in the nature of something though not readily apparent',
                    'children': [
                        {
                            'id': 'implicit.a.0115',
                            'name': 'inexplicit, implicit',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 'a',
                            'examples': "['an implicit agreement not to raise the subject', 'there was implicit criticism in his voice', 'anger was implicit in the argument', 'the oak is implicit in the acorn']",
                            'definition': 'implied though not directly expressed; inherent in the nature of something',
                            'label': '(a)implied though not directly expressed; inherent in the nature of something',
                            'children': []
                        }
                    ]
                },
                {
                    'id': 'silent.s.03',
                    'name': 'understood, tacit, silent',
                    'status': 'G',
                    'relation': 'SimilarTo',
                    'pos': 's',
                    'examples': "['gave silent consent', 'a tacit agreement', 'the understood provisos of a custody agreement']",
                    'definition': 'implied by or inferred from actions or statements',
                    'label': '(s)implied by or inferred from actions or statements',
                    'children': [
                        {
                            'id': 'implicit.a.0117',
                            'name': 'inexplicit, implicit',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 'a',
                            'examples': "['an implicit agreement not to raise the subject', 'there was implicit criticism in his voice', 'anger was implicit in the argument', 'the oak is implicit in the acorn']",
                            'definition': 'implied though not directly expressed; inherent in the nature of something',
                            'label': '(a)implied though not directly expressed; inherent in the nature of something',
                            'children': []
                        }
                    ]
                },
                {
                    'id': 'unexpressed.s.01',
                    'name': 'unspoken, unvoiced, unverbalised, unverbalized, unuttered, unstated, unsaid, unexpressed',
                    'status': 'G',
                    'relation': 'SimilarTo',
                    'pos': 's',
                    'examples': "['the unexpressed terms of the agreement', 'things left unsaid', 'some kind of unspoken agreement', 'his action is clear but his reason remains unstated']",
                    'definition': 'not made explicit',
                    'label': '(s)not made explicit',
                    'children': [
                        {
                            'id': 'implicit.a.0119',
                            'name': 'inexplicit, implicit',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 'a',
                            'examples': "['an implicit agreement not to raise the subject', 'there was implicit criticism in his voice', 'anger was implicit in the argument', 'the oak is implicit in the acorn']",
                            'definition': 'implied though not directly expressed; inherent in the nature of something',
                            'label': '(a)implied though not directly expressed; inherent in the nature of something',
                            'children': []
                        }
                    ]
                },
                {
                    'id': 'explicit.a.0128',
                    'name': 'expressed, explicit',
                    'status': 'G',
                    'relation': 'Antonym',
                    'pos': 'a',
                    'examples': "['explicit instructions', 'she made her wishes explicit', 'explicit sexual scenes']",
                    'definition': 'precisely and clearly expressed or readily observable; leaving nothing to implication',
                    'label': '(a)precisely and clearly expressed or readily observable; leaving nothing to implication',
                    'children': [
                        {
                            'id': 'explicitness.n.0121',
                            'name': 'explicitness',
                            'status': 'G',
                            'relation': 'Attribute',
                            'pos': 'n',
                            'examples': '[]',
                            'definition': 'clarity as a consequence of being explicit',
                            'label': '(n)clarity as a consequence of being explicit',
                            'children': []
                        },
                        {
                            'id': 'declared.s.02',
                            'name': 'stated, declared',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 's',
                            'examples': '[]',
                            'definition': 'declared as fact; explicitly stated',
                            'label': '(s)declared as fact; explicitly stated',
                            'children': []
                        },
                        {
                            'id': 'definitive.s.01',
                            'name': 'unequivocal, definitive',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 's',
                            'examples': "['the plain and unequivocal language of the laws']",
                            'definition': 'clearly defined or formulated; - R.B.Taney',
                            'label': '(s)clearly defined or formulated; - R.B.Taney',
                            'children': []
                        },
                        {
                            'id': 'express.s.01',
                            'name': 'express',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 's',
                            'examples': "['her express wish']",
                            'definition': 'not tacit or implied',
                            'label': '(s)not tacit or implied',
                            'children': []
                        },
                        {
                            'id': 'graphic.s.02',
                            'name': 'graphic',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 's',
                            'examples': "['graphic sexual scenes']",
                            'definition': 'describing nudity or sexual activity in graphic detail',
                            'label': '(s)describing nudity or sexual activity in graphic detail',
                            'children': []
                        },
                        {
                            'id': 'hard-core.s.03',
                            'name': 'hardcore, hard-core',
                            'status': 'G',
                            'relation': 'SimilarTo',
                            'pos': 's',
                            'examples': "['hard-core pornography']",
                            'definition': 'extremely explicit',
                            'label': '(s)extremely explicit',
                            'children': []
                        },
                        {
                            'id': 'implicit.a.0127',
                            'name': 'inexplicit, implicit',
                            'status': 'G',
                            'relation': 'Antonym',
                            'pos': 'a',
                            'examples': "['an implicit agreement not to raise the subject', 'there was implicit criticism in his voice', 'anger was implicit in the argument', 'the oak is implicit in the acorn']",
                            'definition': 'implied though not directly expressed; inherent in the nature of something',
                            'label': '(a)implied though not directly expressed; inherent in the nature of something',
                            'children': []
                        }
                    ]
                }
            ]
        }
    ]
};
const nodeLegend = [
    ["查询词", "text-blue-400"],
    ["释义词", "text-red-400"],
    ["关联词", "text-green-400"],
];
const relationLegend = [
    ["Antonym", "反义词", "text-green-400"],
    ["Attribute", "属性", "text-green-400"],
    ["Cause", "原因", "text-green-400"],
    ["Domain", "领域", "text-green-400"],
    ["Entailment", "蕴含", "text-green-400"],
    ["InSynset", "释义", "text-green-400"],
    ["IsA", "属于", "text-green-400"],
    ["PartOf", "部分", "text-green-400"],
    ["Similar", "相似", "text-green-400"],
];




const colors = {
    B: "#5B8FF9",
    R: "#F46649",
    Y: "#EEBC20",
    G: "#5BD8A6",
    DI: "#A7A7A7",
};
/** @type {import('./$types').PageServerLoad} */
export async function load({ params }) {
    // const response = await fetch('https://gw.alipayobjects.com/os/basement_prod/6cae02ab-4c29-44b2-b1fd-4005688febcb.json');
    // const data = await response.json();
    // if (response) {
    //     return data;
    // }
    // throw error(404, 'Not found');
    return { info: info, nodeLegend: nodeLegend, relationLegend: relationLegend, colors: colors };
}





