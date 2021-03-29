import VueRouter from 'vue-router'
import Main from './components/Main'
import WrapperData from './components/ViewAllData/WrapperData'
import WrapperGraph from './components/Graph/WrapperGraph'
import WrapperAnalysis from './components/Analysis/WrapperAnalysis'
import WrapperCluster from './components/Analysis/WrapperCluster'
import WrapperDangerous from './components/Analysis/WrapperDangerous'


export default new VueRouter({
    routes:[
        {path: '', component:Main},
        {path: '/data', component:WrapperData},
        {path: '/graph', component:WrapperGraph},
        {path: '/violator', component:WrapperAnalysis},
        {path: '/importance', component:WrapperCluster},
        {path: '/dangerous', component:WrapperDangerous},
        
        

    ],
    mode: 'history'
})