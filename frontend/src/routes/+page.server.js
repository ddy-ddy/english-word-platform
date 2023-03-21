/*
 * @Author: ddy 58058861+ddy-ddy@users.noreply.github.com
 * @Date: 2023-03-07 22:23:47
 * @LastEditTime: 2023-03-21 22:42:11
 * @Github: https://github.com/ddy-ddy
 * @Website: https://ddy-ddy.com
 */
import { error } from '@sveltejs/kit';

const info = { 'id': '0', 'nodeType': 'query', 'name': 'implicit', 'status': 'B', 'relation': '', 'pos': '', 'examples': '', 'definition': '', 'children': [{ 'id': 'implicit.s.02', 'name': 'implicit', 'status': 'R', 'relation': 'Has_Lemma', 'pos': 's', 'examples': "['implicit trust']", 'definition': 'being without doubt or reserve', 'label': '(s)being without doubt or reserve', 'children': [] }, { 'id': 'implicit.a.01', 'name': 'implicit', 'status': 'R', 'relation': 'Has_Lemma', 'pos': 'a', 'examples': "['an implicit agreement not to raise the subject', 'there was implicit criticism in his voice', 'anger was implicit in the argument', 'the oak is implicit in the acorn']", 'definition': 'implied though not directly expressed; inherent in the nature of something', 'label': '(a)implied though not directly expressed; inherent in the nature of something', 'children': [{ 'id': 'unexpressed.s.01', 'name': 'unexpressed', 'status': 'G', 'relation': 'SimilarTo', 'pos': 's', 'examples': "['the unexpressed terms of the agreement', 'things left unsaid', 'some kind of unspoken agreement', 'his action is clear but his reason remains unstated']", 'definition': 'not made explicit', 'label': '(s)not made explicit', 'children': [] }, { 'id': 'silent.s.03', 'name': 'silent', 'status': 'G', 'relation': 'SimilarTo', 'pos': 's', 'examples': "['gave silent consent', 'a tacit agreement', 'the understood provisos of a custody agreement']", 'definition': 'implied by or inferred from actions or statements', 'label': '(s)implied by or inferred from actions or statements', 'children': [] }, { 'id': 'implicit_in.s.01', 'name': 'implicit_in', 'status': 'G', 'relation': 'SimilarTo', 'pos': 's', 'examples': "['shortcomings inherent in our approach', 'an underlying meaning']", 'definition': 'in the nature of something though not readily apparent', 'label': '(s)in the nature of something though not readily apparent', 'children': [] }, { 'id': 'explicitness.n.01', 'name': 'explicitness', 'status': 'G', 'relation': 'Attribute', 'pos': 'n', 'examples': '[]', 'definition': 'clarity as a consequence of being explicit', 'label': '(n)clarity as a consequence of being explicit', 'children': [] }, { 'id': 'explicit.a.01', 'name': 'explicit', 'status': 'G', 'relation': 'Antonym', 'pos': 'a', 'examples': "['explicit instructions', 'she made her wishes explicit', 'explicit sexual scenes']", 'definition': 'precisely and clearly expressed or readily observable; leaving nothing to implication', 'label': '(a)precisely and clearly expressed or readily observable; leaving nothing to implication', 'children': [] }] }] };
const nodeLegend = [
    ["查询词", "text-blue-400"],
    ["释义词", "text-red-400"],
    ["关联词", "text-green-400"],
];
const relationLegend = [
    ["Lemmas", "释义", "text-red-400"],
    ["Antonym", "反义", "text-green-400"],
    ["Attribute", "属性", "text-green-400"],
    ["Cause", "造成", "text-green-400"],
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





