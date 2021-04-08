import request from '@/utils/request'

export function login(data) {
  return request({
    // url: '/vue-element-admin/user/login/',
    url: '/user/login/',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    // url: '/vue-element-admin/user/info/',
    url: '/user/info/',
    method: 'get',
    // headers: { 'Authorization': 'Bearer ' + token }
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/user/logout/',
    method: 'post'
  })
}