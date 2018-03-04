import {USER_LOGGED_IN, USER_LOGGED_OUT} from '../types';
import setAuthorizationHeader from '../utils/setAuthorizationHeader';
import api from '../api';

export const userLoggedIn = (user) => ({
  type: USER_LOGGED_IN,
  user
});

export const userLoggedOut = () => ({
  type: USER_LOGGED_OUT
});

export const logout = () => (dispatch) => {
  localStorage.removeItem('coinJWT');
  setAuthorizationHeader();
  dispatch(userLoggedOut());
}

export const login = credentials => (dispatch) =>
  api.user.login(credentials).then(user => {
    localStorage.coinJWT = user.token;
    dispatch(userLoggedIn(user))
  })

export const confirm = (token) => (dispatch) => api.user.verify(token)
  .then(user => {
    localStorage.removeItem('coinJWT');
    setAuthorizationHeader();
    dispatch(userLoggedOut());
  })

export const resetpw = credentials => (dispatch) =>
  api.user.resetpw(credentials)//.then( res => {
    //do something
  // })

export const resetPasswordRequest = ({email}) => () =>
  api.user.resetPasswordRequest(email)
