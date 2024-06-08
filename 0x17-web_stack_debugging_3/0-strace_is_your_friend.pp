# script auto removes wrong php's extention from .phpp to .php
exec { 'correct_php_extension_spelling':
    command => 'sed -i \'s/phpp/php/g\' /var/www/html/wp-settings.php',
    path    => '/bin/'
}
