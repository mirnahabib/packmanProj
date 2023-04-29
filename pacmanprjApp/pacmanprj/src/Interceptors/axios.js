import axios from 'axios';

// //Setting default path to make it simpler for axios tokens
//axios.defaults.baseURL = '/api/auth/'

//For refreshing/closing the browser (unfinished)
axios.interceptors.response.use(resp => resp, async error =>{
    if(error.response.status === 401){
        const response = await axios.post('/api/auth/',{},{withCredentials: true});
        if(response.status === 200){
            axios.defaults.headers.common['Authorization'] = `Bearer ${response.data['token']}`;
            return axios(error.config);
        }
    }
    return error;
});