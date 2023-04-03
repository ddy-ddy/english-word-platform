/*
 * @Author: ddy 58058861+ddy-ddy@users.noreply.github.com
 * @Date: 2023-03-07 22:23:47
 * @LastEditTime: 2023-04-02 22:25:35
 * @Github: https://github.com/ddy-ddy
 * @Website: https://ddy-ddy.com
 */
import { error } from '@sveltejs/kit';

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
    return { nodeLegend: nodeLegend, relationLegend: relationLegend, colors: colors };
}





