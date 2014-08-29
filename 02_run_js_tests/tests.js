QUnit.test('add class to div', 1, function (assert) {
    document.querySelector('#qunit').innerHTML = '<div class="test"></div>';
    document.querySelector('.test').classList.add('tested');
    assert.ok(document.querySelector('#qunit').innerHTML === '<div class="test tested"></div>');
});
