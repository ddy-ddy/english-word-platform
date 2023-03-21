/*
 * @Author: ddy 58058861+ddy-ddy@users.noreply.github.com
 * @Date: 2023-03-07 22:23:47
 * @LastEditTime: 2023-03-21 17:05:48
 * @Github: https://github.com/ddy-ddy
 * @Website: https://ddy-ddy.com
 */
import { error } from '@sveltejs/kit';

const info = {
    id: 'g1',
    nodeType: 'query',
    name: 'implicit',
    label: '',
    status: 'B',
    relation: null,
    children: [
        {
            id: 'g12',
            nodeType: "lemma",
            name: 'implicit',
            label: '(adj) suggested without being directly expressed',
            status: 'R',
            relation: "Has_Lemma",
            children: [
                {
                    id: 'g121',
                    name: 'Name3',
                    nodeType: "lemma",
                    collapsed: true,
                    label: '138.00',
                    status: 'G',
                    relation: "Has_Lemma",
                    children: [
                        {
                            id: 'g1211',
                            nodeType: "lemma",
                            name: 'Name4',
                            label: '138.00',
                            status: 'G',
                            relation: "Has_Lemma",
                            children: [],
                        },
                    ],
                },
                {
                    id: 'g122',
                    nodeType: "lemma",
                    name: 'Name5',
                    collapsed: true,
                    label: '100.00',
                    status: 'G',
                    relation: "Has_Lemma",
                    children: [
                        {
                            id: 'g1221',
                            nodeType: "lemma",
                            name: 'Name6',
                            label: '40.00',
                            status: 'G',
                            relation: "Has_Lemma",
                            children: [
                                {
                                    id: 'g12211',
                                    nodeType: "lemma",
                                    name: 'Name6-1',
                                    label: '40.00',
                                    status: 'G',
                                    relation: "Has_Lemma",
                                    children: [],
                                },
                            ],
                        },
                        {
                            id: 'g1222',
                            nodeType: "lemma",
                            name: 'Name7',
                            label: '60.00',
                            status: 'G',
                            relation: "Has_Lemma",
                            children: [],
                        },
                    ],
                },
                {
                    id: 'g123',
                    nodeType: "lemma",
                    name: 'Name8',
                    collapsed: true,
                    label: '100.00',
                    status: 'G',
                    relation: "Has_Lemma",
                    children: [
                        {
                            id: 'g1231',
                            nodeType: "lemma",
                            name: 'Name8-1',
                            label: '100.00',
                            status: 'G',
                            relation: "Has_Lemma",
                            children: [],
                        },
                    ],
                },
            ],
        },
        {
            id: 'g13',
            nodeType: "lemma",
            name: 'implicit',
            label: '(adj)complete and not doubted',
            status: 'R',
            relation: "Has_Lemma",
            children: [
                {
                    id: 'g131',
                    name: 'Name10',
                    label: '33.90',
                    status: 'G',
                    relation: "Has_Lemma",
                    children: [],
                },
                {
                    id: 'g132',
                    name: 'Name11',
                    label: '67.00',
                    status: 'G',
                    relation: "Has_Lemma",
                    children: [],
                },
            ],
        },
    ],
};
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





