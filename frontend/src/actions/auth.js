import {USER_LOGGED_IN, USER_LOGGED_OUT} from '../types';
import setAuthorizationHeader from '../utils/setAuthorizationHeader'

export const userLoggedOut = () => ({
  type: USER_LOGGED_OUT
});

export const logout = () => (dispatch) => {
  localStorage.removeItem('bookwormJWT');
  setAuthorizationHeader();
  dispatch(userLoggedOut());
}
