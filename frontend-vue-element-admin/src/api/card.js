import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/card/',
    method: 'get',
    params: query
  })
}

export function fetchCard(id) {
  return request({
    url: '/card/' + id + '/',
    method: 'get'
    // params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/card/pv',
    method: 'get',
    params: { pv }
  })
}

export function createCard(data) {
  return request({
    url: '/card/',
    method: 'post',
    data
  })
}

export function updateCard(data, id) {
  return request({
    url: '/card/' + id + '/',
    method: 'put',
    data
  })
}

export function deleteCard(id) {
  return request({
    url: '/card/' + id + '/',
    method: 'delete'
  })
}
