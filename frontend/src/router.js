import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import MecabPosTagger from './views/mecabpostagger.vue';
import MecabSpaceCheck from './views/mecabspacecheck.vue';
import MecabMultiNoun from './views/mecabmultinoun.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home,
        },

        {
            path: '/mecabpostagger',
            name: 'mecabpostagger',
            component: MecabPosTagger,
        },
        {
            path: '/mecabspacecheck',
            name: 'mecabspacecheck',
            component: MecabSpaceCheck,
        },
        {
            path: '/mecabmultinoun',
            name: 'mecabmultinoun',
            component: MecabMultiNoun,
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
        },
    ],
});
