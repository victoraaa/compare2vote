(function () {
    window.PollListViewModel = function(kwargs) {
        this.ui = kwargs.ui;
        this.polls = ko.observableArray();
        this.votingUI = kwargs.votingUI;
    };

    PollListViewModel.prototype = {
        init: function(polls) {
            polls.forEach(function (poll) {
                this.polls.push(new PollViewModel(poll));
            }.bind(this));
            this.votingViewModel = new VotingViewModel();
            ko.applyBindings(this, this.ui.get(0));
            ko.applyBindings(this.votingViewModel, this.votingUI.get(0));
        }
    };

    var PollViewModel = function(poll){
        this.title = ko.observable(poll.title);
        this.question = ko.observable(poll.question);
        this.options = ko.observableArray(poll.options);
        this.numberOfVotes = ko.observable(poll.number_of_votes);
        this.leaders = ko.observableArray(poll.leaders);
        this.editUrl = ko.observable(poll.editUrl);
        this.votingOptionsUrl = ko.observable(poll.votingOptionsUrl);
        this.voteUrl = ko.observable(poll.voteUrl);
    };

    PollViewModel.prototype = {
        newDispute: function(votingView) {
            this.getOptions(function(json) {
                options = json.responseJSON;
                votingView.options(options);
                votingView.voteUrl(this.voteUrl());
                votingView.nextDispute(function () {
                    this.newDispute(votingView);
                }.bind(this));
            }.bind(this));
        },

        getOptions: function(callback) {
            $.ajax({
                url: this.votingOptionsUrl(),
                type: "GET",
                dataType: "json",
                traditional: true,
                complete: callback,
            });
        },
    };

    var VotingViewModel = function() {
        this.options = ko.observableArray([{name: "", image_url: ""}, {name: "", image_url: ""}]);
        this.nextDispute = ko.observable();
        this.voteUrl = ko.observable();
    };

    VotingViewModel.prototype = {
        vote: function(winnerName, loserName) {
            $.ajax({
                url: this.voteUrl(),
                type: "POST",
                data: {json: JSON.stringify({winner: winnerName, loser: loserName})},
                traditional: true,
                success: this.nextDispute(),
            });
        },
    };

    var ChoiceViewModel = function(choice) {

    };

    ChoiceViewModel.prototype = {
        
    };

}) ();
