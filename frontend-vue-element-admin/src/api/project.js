import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/project/',
    method: 'get',
    params: query
  })
}

export function fetchProject(id) {
  return request({
    // url: '/vue-element-admin/article/detail',
    url: '/project/' + id + '/',
    method: 'get'
    // params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    // url: '/vue-element-admin/article/pv',
    url: '/project/pv',
    method: 'get',
    params: { pv }
  })
}

export function createProject(data) {
  return request({
    // url: '/vue-element-admin/article/create',
    url: '/project/',
    method: 'post',
    data
  })
}

export function updateProject(data, id) {
  return request({
    url: '/project/' + id + '/',
    method: 'put',
    data
  })
}

export function deleteProject(id) {
  return request({
    url: '/project/' + id + '/',
    method: 'delete'
  })
}
