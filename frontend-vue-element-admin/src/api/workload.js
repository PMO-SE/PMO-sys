import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/workload/',
    method: 'get',
    params: query
  })
}

export function fetchArticle(id) {
  return request({
    // url: '/vue-element-admin/article/detail',
    url: '/workload/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    // url: '/vue-element-admin/article/pv',
    url: '/workload/pv',
    method: 'get',
    params: { pv }
  })
}

export function createProject(data) {
  return request({
    // url: '/vue-element-admin/article/create',
    url: '/workload/',
    method: 'post',
    data
  })
}

export function updateProject(data, id) {
  return request({
    url: '/workload/' + id + '/',
    method: 'put',
    data
  })
}

export function deleteProject(id) {
  return request({
    url: '/workload/' + id + '/',
    method: 'delete'
  })
}
