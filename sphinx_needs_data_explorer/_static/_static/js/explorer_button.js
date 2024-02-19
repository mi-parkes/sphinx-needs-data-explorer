function initializeLibrary() {
    console.log('explorer_button.js initialized');
    $('#explorer-button').click(function() {
        //alert('Button clicked!');
        var $element = $('a.navbar-brand.logo');
        if ($element.length > 0) {
            var hrefValue = $element.attr('href');            
            var directoryPath = hrefValue.substring(0, hrefValue.lastIndexOf('/') + 1);
            var explorerURL = directoryPath + '_static/sphinx_needs_data_explorer.html';
            var newWindow = window.open(explorerURL,'_blank');
            if (newWindow) {
                newWindow.focus();
            }
            console.log('Href value:', hrefValue);
        } else {
            console.log(`Element '${element}' not found`);
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    initializeLibrary();
});
