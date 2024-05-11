    # Approve the router to spend the token
    token.approve(router, amount_token)

    # Add liquidity
    router.addLiquidityETH(
        token,
        amount_token,
        amount_eth_min,
        amount_token_min,
        msg.sender,
        block.timestamp + 3600
    )
