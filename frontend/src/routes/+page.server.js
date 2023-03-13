/*
 * @Author: ddy 58058861+ddy-ddy@users.noreply.github.com
 * @Date: 2023-03-07 22:23:47
 * @LastEditTime: 2023-03-13 10:53:33
 * @Github: https://github.com/ddy-ddy
 * @Website: https://ddy-ddy.com
 */
import { error } from '@sveltejs/kit';

// mocked data
const data = {
    id: 'g1',
    name: 'Name1',
    count: 123456,
    label: '538.90',
    currency: 'Yuan',
    rate: 1.0,
    status: 'B',
    variableName: 'V1',
    variableValue: 0.341,
    variableUp: false,
    children: [
        {
            id: 'g12',
            name: 'Deal with LONG label LONG label LONG label LONG label',
            count: 123456,
            label: '338.00',
            rate: 0.627,
            status: 'R',
            currency: 'Yuan',
            variableName: 'V2',
            variableValue: 0.179,
            variableUp: true,
            children: [
                {
                    id: 'g121',
                    name: 'Name3',
                    collapsed: true,
                    count: 123456,
                    label: '138.00',
                    rate: 0.123,
                    status: 'B',
                    currency: 'Yuan',
                    variableName: 'V2',
                    variableValue: 0.27,
                    variableUp: true,
                    children: [
                        {
                            id: 'g1211',
                            name: 'Name4',
                            count: 123456,
                            label: '138.00',
                            rate: 1.0,
                            status: 'B',
                            currency: 'Yuan',
                            variableName: 'V1',
                            variableValue: 0.164,
                            variableUp: false,
                            children: [],
                        },
                    ],
                },
                {
                    id: 'g122',
                    name: 'Name5',
                    collapsed: true,
                    count: 123456,
                    label: '100.00',
                    rate: 0.296,
                    status: 'G',
                    currency: 'Yuan',
                    variableName: 'V1',
                    variableValue: 0.259,
                    variableUp: true,
                    children: [
                        {
                            id: 'g1221',
                            name: 'Name6',
                            count: 123456,
                            label: '40.00',
                            rate: 0.4,
                            status: 'G',
                            currency: 'Yuan',
                            variableName: 'V1',
                            variableValue: 0.135,
                            variableUp: true,
                            children: [
                                {
                                    id: 'g12211',
                                    name: 'Name6-1',
                                    count: 123456,
                                    label: '40.00',
                                    rate: 1.0,
                                    status: 'R',
                                    currency: 'Yuan',
                                    variableName: 'V1',
                                    variableValue: 0.181,
                                    variableUp: true,
                                    children: [],
                                },
                            ],
                        },
                        {
                            id: 'g1222',
                            name: 'Name7',
                            count: 123456,
                            label: '60.00',
                            rate: 0.6,
                            status: 'G',
                            currency: 'Yuan',
                            variableName: 'V1',
                            variableValue: 0.239,
                            variableUp: false,
                            children: [],
                        },
                    ],
                },
                {
                    id: 'g123',
                    name: 'Name8',
                    collapsed: true,
                    count: 123456,
                    label: '100.00',
                    rate: 0.296,
                    status: 'DI',
                    currency: 'Yuan',
                    variableName: 'V2',
                    variableValue: 0.131,
                    variableUp: false,
                    children: [
                        {
                            id: 'g1231',
                            name: 'Name8-1',
                            count: 123456,
                            label: '100.00',
                            rate: 1.0,
                            status: 'DI',
                            currency: 'Yuan',
                            variableName: 'V2',
                            variableValue: 0.131,
                            variableUp: false,
                            children: [],
                        },
                    ],
                },
            ],
        },
        {
            id: 'g13',
            name: 'Name9',
            count: 123456,
            label: '100.90',
            rate: 0.187,
            status: 'B',
            currency: 'Yuan',
            variableName: 'V2',
            variableValue: 0.221,
            variableUp: true,
            children: [
                {
                    id: 'g131',
                    name: 'Name10',
                    count: 123456,
                    label: '33.90',
                    rate: 0.336,
                    status: 'R',
                    currency: 'Yuan',
                    variableName: 'V1',
                    variableValue: 0.12,
                    variableUp: true,
                    children: [],
                },
                {
                    id: 'g132',
                    name: 'Name11',
                    count: 123456,
                    label: '67.00',
                    rate: 0.664,
                    status: 'G',
                    currency: 'Yuan',
                    variableName: 'V1',
                    variableValue: 0.241,
                    variableUp: false,
                    children: [],
                },
            ],
        },
        {
            id: 'g14',
            name: 'Name12',
            count: 123456,
            label: '100.00',
            rate: 0.186,
            status: 'G',
            currency: 'Yuan',
            variableName: 'V2',
            variableValue: 0.531,
            variableUp: true,
            children: [],
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