import Cookies from 'js-cookie'

export function getToken(TokenKey = 'Access-token') {
  return Cookies.get(TokenKey)
}

export function setToken(TokenKey = 'Access-token', token) {
  return Cookies.set(TokenKey, token)
}

export function removeToken(TokenKey = 'Access-token') {
  return Cookies.remove(TokenKey)
}
