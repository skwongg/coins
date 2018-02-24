import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
    user: {
      login: (credentials) =>
        axios.post('/api/auth/', {credentials}).then(res => {
          return JSON.parse(res.data)
        })
    }
};
