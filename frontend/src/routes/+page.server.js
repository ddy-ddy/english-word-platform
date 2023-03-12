/*
 * @Author: ddy 58058861+ddy-ddy@users.noreply.github.com
 * @Date: 2023-03-07 22:23:47
 * @LastEditTime: 2023-03-12 22:12:47
 * @Github: https://github.com/ddy-ddy
 * @Website: https://ddy-ddy.com
 */
import { error } from '@sveltejs/kit';

const data = {
    id: "A",
    children: [
        {
            id: "A1",
            children: [
                { id: "A11" },
                { id: "A12" },
                { id: "A13" },
                { id: "A14" },
            ],
        },
        {
            id: "A2",
            children: [
                {
                    id: "A21",
                    children: [{ id: "A211" }, { id: "A212" }],
                },
                {
                    id: "A22",
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