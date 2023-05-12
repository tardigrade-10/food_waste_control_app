window.addEventListener('load', function() {
    // Attach event listener to delete buttons
    var deleteForms = document.getElementsByClassName('delete-form');
    for (var i = 0; i < deleteForms.length; i++) {
        deleteForms[i].addEventListener('submit', function(e) {
            var confirmDelete = confirm('Are you sure you want to delete this item?');
            if (!confirmDelete) {
                e.preventDefault();
            }
        });
    }
});
