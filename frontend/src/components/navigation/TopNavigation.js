import React from 'react';
import PropTypes from 'prop-types'
import { Menu, Dropdown, Image } from 'semantic-ui-react';
import { connect } from 'react-redux'
import { Link } from 'react-router-dom';
import gravatarUrl from 'gravatar-url';
import * as actions from '../../actions/auth';


const TopNavigation = ({ user, logout, hasBooks }) => {
  return (<Menu secondary pointing>
    <Menu.Item as={Link} to='/dashboard'>Dashboard</Menu.Item>

    {hasBooks && <Menu.Item as={Link} to='/coins'>Coins</Menu.Item>}

    <Menu.Menu position="right">
      <Dropdown trigger={<Image avatar src={gravatarUrl('a@b.com')} />}>
        <Dropdown.Menu>
          <Dropdown.Item onClick={() => logout()}>Logout</Dropdown.Item>
        </Dropdown.Menu>
      </Dropdown>
    </Menu.Menu>
  </Menu>)
}

TopNavigation.propTypes = {
  user: PropTypes.shape({
    email: PropTypes.string.isRequired
  }).isRequired,
  hasBooks: PropTypes.bool.isRequired,
  logout: PropTypes.func.isRequired
}

function mapStateToProps(state){
  return {
    user: state.user,
    hasBooks: 1 //#TODO: allBooksSelector(state).length > 0
  }
}

export default connect(mapStateToProps, { logout: actions.logout })(TopNavigation);
