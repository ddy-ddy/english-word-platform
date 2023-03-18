/*
 * @Author: ddy 58058861+ddy-ddy@users.noreply.github.com
 * @Date: 2023-03-07 22:23:47
 * @LastEditTime: 2023-03-18 22:41:13
 * @Github: https://github.com/ddy-ddy
 * @Website: https://ddy-ddy.com
 */
import { error } from '@sveltejs/kit';

// mocked data
const data = {
    id: 'g1',
    nodeType: 'query',
    name: 'implicit',
    label: '',
    status: 'B',
    children: [
        {
            id: 'g12',
            nodeType: "lemma",
            name: 'implicit',
            label: '(adj) suggested without being directly expressed',
            status: 'R',
            children: [
                {
                    id: 'g121',
                    name: 'Name3',
                    nodeType: "lemma",
                    collapsed: true,
                    label: '138.00',
                    status: 'G',
                    children: [
                        {
                            id: 'g1211',
                            nodeType: "lemma",
                            name: 'Name4',
                            label: '138.00',
                            status: 'G',
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
                    children: [
                        {
                            id: 'g1221',
                            nodeType: "lemma",
                            name: 'Name6',
                            label: '40.00',
                            status: 'G',
                            children: [
                                {
                                    id: 'g12211',
                                    nodeType: "lemma",
                                    name: 'Name6-1',
                                    label: '40.00',
                                    status: 'G',
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
                    children: [
                        {
                            id: 'g1231',
                            nodeType: "lemma",
                            name: 'Name8-1',
                            label: '100.00',
                            status: 'G',
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
            children: [
                {
                    id: 'g131',
                    name: 'Name10',
                    label: '33.90',
                    status: 'G',
                    children: [],
                },
                {
                    id: 'g132',
                    name: 'Name11',
                    label: '67.00',
                    status: 'G',
                    children: [],
                },
            ],
        },
    ],
};
/** @type {import('./$types').PageServerLoad} */
export async function load({ params }) {
    // const response = await fetch('https://gw.alipayobjects.com/os/basement_prod/6cae02ab-4c29-44b2-b1fd-4005688febcb.json');
    // const data = await response.json();
    // if (response) {
    //     return data;
    // }
    // throw error(404, 'Not found');
    return data;
}