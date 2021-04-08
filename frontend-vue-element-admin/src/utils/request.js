import axios from 'axios'
import { MessageBox, Message } from 'element-ui'
import store from '@/store'
import { getToken, setToken } from '@/utils/auth'

// create an axios instance
const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 5000 // request timeout
})

// request interceptor
service.interceptors.request.use(
  async config => {
    if (store.getters.token) {
      config.headers['Authorization'] = 'Bearer ' + getToken('Access-token')
    }
    return config
  },
  error => {
    // do something with request error
    console.log(error) // for debug
    return Promise.reject(error)
  }
)

// response interceptor
service.interceptors.response.use(
  /**
   * If you want to get http information such as headers or status
   * Please return  response => response
  */

  /**
   * Determine the request status by custom code
   * Here is just an example
   * You can also judge the status by HTTP Status Code
   */
  response => {
    const res = response.data
    // 不太正常
    if (res.code !== 20000) {
      // 50008: Invalid token; 50012: Other clients logged in;
      if (res.code === '50008' || res.code === 50008) {
        // to re-login
        MessageBox.confirm('You have been logged out, you can cancel to stay on this page, or log in again', 'Confirm logout', {
          confirmButtonText: 'Re-Login',
          cancelButtonText: 'Cancel',
          type: 'warning'
        }).then(() => {
          store.dispatch('user/resetToken').then(() => {
            location.reload()
          })
        })
      }
      console.log(res.code)
      return Promise.reject(new Error(res.message || 'Error'))
    } else {
      // 完全正常
      axios({
        method: 'post',
        url: 'dev-api/user/token/refresh/',
        data: { 'refresh': getToken('Refresh-token') }
      }).then(res_data => {
        if (res_data.data.code === 20000) {
          setToken('Access-token', res_data.data.data.access)
          console.log('Access-token已经刷新')
        } else {
          console.log('Refresh-token过期')
          return Promise.reject(new Error({ message: 'Refresh-token过期' }))
        }
      })
      return res
    }
  },
  error => {
    console.log('err' + error) // for debug
    Message({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    })
    return Promise.reject(error)
  }
)

export default service
