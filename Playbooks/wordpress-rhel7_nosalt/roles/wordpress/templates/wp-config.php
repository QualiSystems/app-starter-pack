<?php
/**
 * The base configurations of the WordPress.
 *
 * This file has the following configurations: MySQL settings, Table Prefix,
 * Secret Keys, WordPress Language, and ABSPATH. You can find more information
 * by visiting {@link http://codex.wordpress.org/Editing_wp-config.php Editing
 * wp-config.php} Codex page. You can get the MySQL settings from your web host.
 *
 * This file is used by the wp-config.php creation script during the
 * installation. You don't have to use the web site, you can just copy this file
 * to "wp-config.php" and fill in the values.
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', '{{ wp_db_name }}');

/** MySQL database username */
define('DB_USER', '{{ wp_db_user }}');

/** MySQL database password */
define('DB_PASSWORD', '{{ wp_db_password }}');

/** MySQL hostname */
define('DB_HOST', '{{groups['database'][0]}}:{{ mysql_port }}');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */

define('AUTH_KEY',         '0MvUCj#uDTcffO1f%p*hu2S:t|ZTVE*t0-u4P` :]o@M~(XJE}0;U}+Vj}F@yzTY');
define('SECURE_AUTH_KEY',  '}KrrVMxCIEN-,;QORP-?SdfQ$NcM9kT+,Jn~|q:(Ob)ap+d8/JPd|?@hbH+NP=Bj');
define('LOGGED_IN_KEY',    '.ZR-)/iG?d+-$o$LB||~0$U9505d~dfpRF$sTjD@s+F*!@RR-&wS&>72j3#OSE}c');
define('NONCE_KEY',        'U2EZ7U-s>`BpXW)[+mw*}-V)LYQsz*uFd|[wey|Jm:qY!t_}w6G2Y&,S6o-0(?BF');
define('AUTH_SALT',        'YnBH4R}Z^<bXL&jD}-$ZynO6$!ahXR= pl&u?_CO-]f)K1*@3RxMy9z9+6D!nw(m');
define('SECURE_AUTH_SALT', 'VM 5~_-VF#|h&LFY)J#h#O& D@K5is6a[<|Y+uCv/CX;a|6IZ<Q92X;y~uD9ySAY');
define('LOGGED_IN_SALT',   ':`jRQq1OMZy}|oiykTA}aRh,!r_dyy[S{0s@~PRlPdW;=FQ}U[R_lhcO=PF_j&y}');
define('NONCE_SALT',       'e2VCSkdu*#7+|khK].aCN8B2P_&bpd.7d}~^J<BmS%+JfH8n9&Xh [w7vzhF^;/W');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each a unique
 * prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * WordPress Localized Language, defaults to English.
 *
 * Change this to localize WordPress. A corresponding MO file for the chosen
 * language must be installed to wp-content/languages. For example, install
 * de_DE.mo to wp-content/languages and set WPLANG to 'de_DE' to enable German
 * language support.
 */
define('WPLANG', '');

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 */
define('WP_DEBUG', false);

/** Disable Automatic Updates Completely */
define( 'AUTOMATIC_UPDATER_DISABLED', {{auto_up_disable}} );

/** Define AUTOMATIC Updates for Components. */
define( 'WP_AUTO_UPDATE_CORE', {{core_update_level}} );

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
